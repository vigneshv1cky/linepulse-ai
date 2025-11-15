import streamlit as st
from src.data_loader import load_and_prepare
from src.kpi_engine import compute_kpis
from src.summary_formatter import format_kpis_for_llm
from src.charts import downtime_by_type_chart, downtime_by_machine_chart
from src.llm_client import call_llm_chat

st.set_page_config(page_title="LinePulse AI", layout="wide")
st.title("LinePulse AI – Downtime Intelligence Copilot")

# Init session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # list of {"role": "user"/"assistant", "content": "..."}
if "summary_text" not in st.session_state:
    st.session_state.summary_text = None
if "file_loaded" not in st.session_state:
    st.session_state.file_loaded = False

uploaded = st.file_uploader("Upload manufacturing downtime CSV", type=["csv"])

if uploaded is not None:
    # Load only when a file is present
    df = load_and_prepare(uploaded)
    kpis = compute_kpis(df)
    summary_text = format_kpis_for_llm(kpis)
    st.session_state.summary_text = summary_text
    st.session_state.file_loaded = True

    st.subheader("Quick KPIs")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Downtime (min)", f"{kpis['total_downtime_minutes']:.1f}")
    col2.metric("Total Downtime (hrs)", f"{kpis['total_downtime_hours']:.2f}")
    col3.metric("Date Range", f"{kpis['date_range']['min_date']} → {kpis['date_range']['max_date']}")

    st.subheader("Downtime by Type")
    st.plotly_chart(downtime_by_type_chart(kpis), use_container_width=True)

    st.subheader("Downtime by Machine")
    st.plotly_chart(downtime_by_machine_chart(kpis), use_container_width=True)

    st.subheader("Downtime summary used by the AI")
    st.text(summary_text)

    st.subheader("Chat with LinePulse AI")
    st.caption(
        "LinePulse automatically generates an initial decision summary. "
        "Then you can ask follow-up questions (e.g., 'focus only on quick wins', "
        "'drill down into Machine 2', 'rewrite this for management')."
    )

    # 🔥 AUTO-GENERATE BASELINE DECISIONS IF NO HISTORY YET
    if st.session_state.chat_history == [] and st.session_state.summary_text:
        with st.spinner("Generating baseline decisions from downtime data…"):
            # Seed chat history with an implicit user request
            initial_user_msg = {
                "role": "user",
                "content": (
                    "Based only on this downtime summary, provide a full decision-focused analysis: "
                    "identify main bottlenecks, recommend 3–5 key decisions, "
                    "give a 7-day action plan, and describe risks if we do nothing."
                ),
            }
            st.session_state.chat_history.append(initial_user_msg)

            initial_response = call_llm_chat(st.session_state.summary_text, st.session_state.chat_history)

            st.session_state.chat_history.append({"role": "assistant", "content": initial_response})

    # 🗨️ Render chat history (including auto-generated baseline decisions)
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 💬 New user question
    user_input = st.chat_input("Ask a follow-up about these decisions or this downtime data…")

    if user_input:
        # Add user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking through the best decisions…"):
                ai_response = call_llm_chat(st.session_state.summary_text, st.session_state.chat_history)
                st.markdown(ai_response)

        # Store AI message
        st.session_state.chat_history.append({"role": "assistant", "content": ai_response})

else:
    st.info("Upload `manufacturing-machine-downtime-logs.csv` to start the analysis.")
    st.session_state.summary_text = None
    st.session_state.chat_history = []
    st.session_state.file_loaded = False

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise RuntimeError("OPENAI_API_KEY not set. Check your .env file or environment variables.")

client = OpenAI(api_key=api_key)


def call_llm_chat(summary_text: str, chat_history: list[dict]) -> str:
    """
    summary_text: fixed downtime KPI summary for this dataset
    chat_history: list of {"role": "user"/"assistant", "content": "..."}
    """

    system_role = {
        "role": "system",
        "content": (
            "You are a senior Industrial Engineer and reliability leader. "
            "Your job is NOT just to describe the data, but to recommend concrete decisions.\n\n"
            "You are given a summary of machine downtime logs from a manufacturing plant. "
            "Using ONLY that data and logical reasoning, you must:\n"
            "1) Identify the main bottlenecks.\n"
            "2) Explain likely root causes in simple, non-jargon language.\n"
            "3) Propose 3–5 clear DECISIONS the plant should make (what to prioritize, where to focus, what to stop/continue/change).\n"
            "4) Turn those decisions into specific actions with expected impact on downtime, cost, or reliability.\n"
            "5) Distinguish between QUICK WINS (0–7 days), NEAR-TERM (1–4 weeks), and LONGER-TERM (>1 month) improvements.\n\n"
            "Always answer using this structure:\n"
            "### Decision Summary (Top 3–5)\n"
            "- DO: <decision>\n"
            "  IMPACT: <expected effect based on data>\n\n"
            "### Recommendations by Area\n"
            "- Machines/Assets:\n"
            "- Maintenance/Spare Parts:\n"
            "- Process / Standard Work:\n"
            "- People / Training:\n\n"
            "### 7-Day Action Plan\n"
            "- Day 1–2: ...\n"
            "- Day 3–5: ...\n"
            "- Day 6–7: ...\n\n"
            "### Risks If No Action Is Taken\n"
            "- ...\n\n"
            "Be specific and practical. Avoid generic advice like 'improve maintenance' or 'monitor performance'. "
            "Tie each recommendation back to patterns in the downtime summary (machines, downtime types, locations, or causes)."
        ),
    }

    data_context = {"role": "system", "content": "Downtime data summary:\n" + summary_text}

    messages = [system_role, data_context]
    messages.extend(chat_history)

    response = client.chat.completions.create(model="gpt-4.1-mini", messages=messages, max_tokens=900, temperature=0.35)
    return response.choices[0].message.content.strip()

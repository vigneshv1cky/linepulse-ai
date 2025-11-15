
# 🟩 LinePulse AI

### **AI-Powered Downtime Intelligence & Decision Copilot for Manufacturing**

LinePulse AI transforms raw manufacturing downtime logs into **clear decisions**, **prioritized actions**, and a **7-day improvement plan**—all powered by AI.

Instead of asking the system what to do, LinePulse AI automatically analyzes your data the moment you upload it and tells you:

* **what’s causing downtime**,
* **what decisions to make next**,
* **what actions have the highest ROI**,
* **what risks you face if you don’t act**,
* **and how to improve reliability this week.**

This makes LinePulse AI a **true Industrial AI Copilot**, not just a chatbot.

---

## 🧠 Why LinePulse AI?

Industrial teams still spend hours slicing downtime logs in Excel or Power BI. LinePulse AI eliminates this by:

* Automatically processing downtime logs
* Computing key KPIs
* Summarizing the data
* Running an AI-powered decision engine
* Providing actionable recommendations instantly
* Supporting multi-turn conversations on the same dataset

No prompt engineering.
No analytics expertise required.
Upload → Decide → Improve.

---

## 🚀 Key Features

### ✅ **1. Automatic Decision Summary (No Prompt Needed)**

As soon as a CSV is uploaded, LinePulse AI generates:

* Top 3–5 decisions to take
* Root cause insights
* Area-based recommendations
* 7-day action plan
* Risks of doing nothing

### ✅ **2. Multi-Turn AI Conversation**

Continue asking follow-up questions like:

* “Give me only quick wins.”
* “Drill deeper into Machine 2.”
* “Rewrite as an executive email.”
* “Build a cost-savings estimate.”

The AI remembers the conversation and stays focused on your data.

### ✅ **3. Automatic KPI Extraction**

From downtime logs, the system computes:

* Total downtime (min/hrs)
* Top downtime types
* Worst machines
* Worst locations
* Planned vs unplanned downtime
* Top causes
* Date range

### ✅ **4. Data Visualization**

Plotly charts show:

* Downtime by type
* Downtime by machine

### ✅ **5. Clean, Structured Prompts for Industrial Reasoning**

LinePulse AI follows a strict format:

* **Decision Summary**
* **Area-Wise Recommendations**
* **7-Day Action Plan**
* **Risks If No Action Is Taken**

This ensures consistency and clarity every time.

---

## 📂 Project Structure

```
linepulse-ai/
├── app.py
├── src/
│   ├── data_loader.py
│   ├── kpi_engine.py
│   ├── summary_formatter.py
│   ├── prompts.py
│   ├── llm_client.py
│   └── charts.py
├── manufacturing-machine-downtime-logs.csv
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Streamlit** (frontend + UI)
* **Pandas** (data processing)
* **Plotly** (interactive charts)
* **OpenAI GPT-4.x or GPT-3.5 models** (LLM backend)
* **Session-based chat memory** (multi-turn conversations)

---

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/vigneshv1cky/linepulse-ai.git

cd linepulse-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Add your OpenAI key in .env and Run the app:

```bash
streamlit run app.py
```

---

## 📤 How to Use

1. Launch the app
2. Upload a downtime CSV (example included in `/data`)
3. Instantly see:

   * KPIs
   * Charts
   * Automatic decision summary
4. Ask follow-up questions in the chat

---

## 🔮 Future Enhancements

* Add full **RAG** with:

  * Work orders
  * SOPs
  * OEM manuals
  * Historical downtime
* Predictive recommendations using ML models
* Cost-impact estimation
* Shift-based performance insights
* Integration with plant MES/ERP systems

---

## 🤝 Contribution

Pull requests are welcome!
If you have ideas for improving industrial decision automation, open an issue.

---

## 📜 License

MIT License.

---

## ⭐ Acknowledgements

Built for the **IndustrialEngineer.ai Vibe Coding Hackathon**.
Designed to help factories reduce downtime with AI you can trust.

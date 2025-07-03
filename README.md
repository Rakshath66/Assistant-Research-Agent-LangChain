---
title: Rag Agent Ui
emoji: 🚀
colorFrom: red
colorTo: red
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: Google-style web search, ask questions, Memory-aware convo
license: mit
---
Here's a polished, professional, and **open-source–friendly GitHub `README.md`** that includes everything from project intro to contribution steps and MIT license, tailored to attract contributors:

---

````markdown
# 🔎 Assistant Research Agent — LangChain + Mistral + Streamlit

A smart **multi-tool AI research assistant** that reads PDFs, searches the web, queries Wikipedia, solves math, and explains every step it takes — all using LangChain Agents and Mistral-7B via OpenRouter.

> ✅ Built with: `LangChain`, `Streamlit`, `Mistral-7B`, `Tavily`, `PyMuPDF`, `Wikipedia`, `PythonREPL`

![GitHub Repo stars](https://img.shields.io/github/stars/your-username/assistant-research-agent?style=social)
![GitHub forks](https://img.shields.io/github/forks/your-username/assistant-research-agent?style=social)
![MIT License](https://img.shields.io/github/license/your-username/assistant-research-agent)

---

## 📸 Preview

![screenshot](demo/screenshot.png) <!-- Add your screenshot here -->

---

## 🧠 Features

- 📄 **Summarize PDFs** using PyMuPDF and an LLM
- 🌐 **Web search** powered by [Tavily](https://tavily.com/)
- 📚 **Wikipedia facts** summarizer
- 🧮 **Python-based calculator** (LangChain’s REPL tool)
- 🔁 **Reverse tool** (custom)
- 💬 **Memory support** for multi-turn conversations
- 🔍 **Reasoning trace** (Thought → Action → Result)
- 🎨 Sleek UI with gradient title and tool checklist

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.9+
- API Keys from:
  - [OpenRouter](https://openrouter.ai)
  - [Tavily](https://app.tavily.com)

---

### 🖥️ Local Installation

```bash
# 1. Clone this repo
git clone https://github.com/your-username/assistant-research-agent.git
cd assistant-research-agent

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API keys in .env
echo "OPENROUTER_API_KEY=your_openrouter_key" >> .env
echo "TAVILY_API_KEY=your_tavily_key" >> .env

# 5. Launch the app
streamlit run src/streamlit_app.py
````

---

## 🗂️ Project Structure

```
assistant-research-agent/
│
├── .streamlit/              # Streamlit config
│   └── config.toml
├── src/
│   ├── streamlit_app.py     # Main UI and agent setup
│   └── agent_tools.py       # Custom LangChain tools
├── requirements.txt         # All Python dependencies
├── .env.example             # Sample env format
└── README.md
```

---

## 🔐 Environment Variables

Create a `.env` file (or set in Streamlit Secrets):

```
OPENROUTER_API_KEY=your_openrouter_key
TAVILY_API_KEY=your_tavily_key
```

If you're using **Streamlit Cloud**, paste this into **Settings → Secrets**:

```toml
OPENROUTER_API_KEY = "sk-..."
TAVILY_API_KEY = "tvly-..."
```

---

## 🧪 Sample Questions

* “What projects did Rakshath work on in the uploaded PDF?”
* “Summarize Wikipedia on LangChain.”
* “Who is Elon Musk? Square the number of years since his birth.”
* “Reverse the string ‘LangChain Rocks!’”

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### ✅ To Contribute:

1. Fork this repository
2. Clone your fork:
   `git clone https://github.com/your-username/assistant-research-agent.git`
3. Create a new branch:
   `git checkout -b feature/my-feature`
4. Make your changes and commit:
   `git commit -m "Add: your message here"`
5. Push to your branch:
   `git push origin feature/my-feature`
6. Open a Pull Request with a description of your changes

> 📢 Please write clean, readable code and include docstrings if adding tools or modifying behavior.

---

## 📦 Deployment Options

### Option 1: Run Locally (Best for Development)

```
streamlit run src/streamlit_app.py
```

### Option 2: [Deploy to Streamlit Cloud](https://streamlit.io/cloud)

1. Fork this repo
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click **New app → From GitHub**
4. Add your repo and branch
5. Under **Advanced Settings → Secrets**, paste your API keys
6. Done!

---

## 📃 License

MIT License © [Your Name](https://github.com/your-username)

```text
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software... [rest of MIT license]
```

---

## ⭐ Star this project if you like it!

It helps others discover it, and motivates me to build more free AI tools.
Also, feel free to open issues, request features, or contribute.

---

### 🧑‍💻 Built by [Your Name](https://github.com/your-username)

* Inspired by modern AI research assistants
* Designed for clarity, transparency, and tool-powered reasoning
* Open-sourced to help others learn LangChain agents

---

```

> Replace:
- `your-username` with your GitHub username
- Add actual screenshot in `demo/screenshot.png` or remove that line
- Fill your real name or link

Would you like me to generate a matching `LICENSE` file (MIT)?
```



Next What?
Here's our **full roadmap after a working RAG Agent** plan

---

### ✅ PHASE 1: ✅ DONE

**You’ve completed:**

* ✅ Tool-based reasoning agent (PDF, Web, Wikipedia, Calculator)
* ✅ Streamlit UI with memory, CoT trace, and tool usage breakdown

---

### 🚀 PHASE 2: Chain-of-Tools Agent

Make your agent **auto-chain** actions like:

> “Summarize top 3 news articles about XYZ”
> ⟶ Search → Pick top links → Read + Summarize → Combine

#### 🔧 Add next tools:

* `summarize_url` (for reading links)
* `multi_url_summary` (loops through list of URLs)
* `web_search_chain` (Tavily + summarize\_url combined)

---

### 🧠 PHASE 3: Agent with Function Memory

Let your agent **remember key facts per user**, like:

> “Who is the CEO of Tesla?”
> → Even next day, it remembers your earlier query.

Use:

* LangChain’s `VectorStoreRetrieverMemory`
* Store extracted facts like Q/A or timeline

---

### 📁 PHASE 4: Document Q\&A + Chunk Tracking

Improve document tool:

* Show which **chunks** were used to generate the answer
* Highlight matching parts in the PDF
* Support **multiple PDFs at once** intelligently

---

### 🤖 PHASE 5: Tool-Using Assistant API

Package your whole logic into:

* `fastapi` or `litestar` backend
* Add endpoint: `/ask` → returns final answer + reasoning trace
* Ideal for chatbot or research assistant SaaS

---

### 🌐 PHASE 6: Assistant with Browsing + Plugin Tools

Use LangGraph (for branching logic) or LangChain Expression Language (LCEL):

* Agent decides: Search? Read? Combine? Skip?
* Add tools like `YouTubeTranscriptTool`, `Google Scholar Reader`, etc.

---


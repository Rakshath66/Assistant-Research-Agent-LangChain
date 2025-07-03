# 🔎 Assistant Research Agent — LangChain + Mistral + Streamlit

A smart **multi-tool AI research assistant** that reads PDFs, searches the web, queries Wikipedia, solves math, and explains every step it takes — all using LangChain Agents and Mistral-7B via OpenAI.

> ✅ Built with: `LangChain`, `Streamlit`, `Mistral-7B`, `Tavily`, `PyMuPDF`, `Wikipedia`, `PythonREPL`

![GitHub Repo stars](https://img.shields.io/github/stars/your-username/assistant-research-agent?style=social)
![GitHub forks](https://img.shields.io/github/forks/your-username/assistant-research-agent?style=social)
![MIT License](https://img.shields.io/github/license/your-username/assistant-research-agent)

---

## 📸 Preview

![screenshot](demo/screenshot.png) <!-- Add your screenshot here -->

---

## 🧠 Features

- 📄 Summarize **PDFs**
- 🌐 Search the **Web** using Tavily
- 📚 Get facts from **Wikipedia**
- 🧮 Solve **math** with Python REPL
- 🔁 Custom **reverse tool**
- 💬 Multi-turn **memory**
- 🪄 Shows **Chain-of-Thought** (Thought → Action → Result)
- ✅ Tool usage checklist
- 🎨 Clean Streamlit UI

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
echo "OPENAI_API_KEY=your_openai_key" >> .env
echo "TAVILY_API_KEY=your_tavily_key" >> .env

# 5. Launch the app
streamlit run src/streamlit_app.py
````

---

## 🗂️ Project Structure

```
assistant-research-agent/
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
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
```

If you're using **Streamlit Cloud**, paste this into **Settings → Secrets**:

```toml
OPENAI_API_KEY = "sk-..."
TAVILY_API_KEY = "tvly-..."
```

---

## 🧪 Try Questions Like

* “What projects did Rakshath work on in the uploaded PDF?”
* “Summarize Wikipedia on LangChain.”
* “Who is Elon Musk? Square the number of years since his birth.”
* “Reverse the string ‘LangChain Rocks!’”

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### ✅ Steps To Contribute:

1. Fork this repository
2. Clone your fork:
   `git clone https://github.com/rakshath66/assistant-research-agent.git`
3. Create a new branch:
   `git checkout -b feature/my-feature`
4. Make your changes, commit, and push:
   `git commit -m "Add: my feature"`
   `git push origin feature/my-feature`
5. Open a Pull Request with a description of your changes

> 🔍 Please write clean readable code, add docstrings if needed, and test your features!

---

## 📃 License

MIT License © [Rakshath U Shetty](https://github.com/rakshath66)

```text
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software... [rest of MIT license]
```

---

## ⭐ Star this project if you like it!

It helps others discover it, and motivates me to build more free AI tools.
Also, feel free to open issues, request features, or contribute.

---

### 🧑‍💻 Built by [Rakshath U Shetty](https://github.com/rakshath66)

* Open source forever
* Designed for learning, research, and practical use
* Reach out via issues or PRs — ideas welcome!

---

What Next?
This project is just the beginning. We’re building a **production-ready RAG Agent** that evolves over time. Here's the full roadmap after completing the basic agent.

## 📅 Roadmap

---

### ✅ Phase 1: Tool-Based RAG Agent — ✅ Done

* 🧠 Chain-of-Thought Agent using LangChain
* 🔧 Tools: PDF summarization, Web search (Tavily), Wikipedia, Calculator
* 🧮 Built-in Memory
* 💡 Reasoning trace (Thought → Action → Result)
* 🎨 Streamlit UI with tool checklist

---

### 🚀 PHASE 2: Chain-of-Tools Agent

Let the agent auto-chain steps like:

> “Summarize top 3 news articles about XYZ”  
> ⟶ Search → Pick top links → Read + Summarize → Combine insights

#### 🔧 New Tools to Add:

- `summarize_url` — Read and summarize a web page
- `multi_url_summary` — Loop over list of URLs and extract key info
- `web_search_chain` — Combined search + read + summarize

---

### 🧠 PHASE 3: Agent with Function Memory

Let the agent **remember facts** about the user or previous answers.

Example:

> “Who is the CEO of Tesla?”  
> → Even tomorrow, it remembers your earlier query.

🧰 Tools & Techniques:

- LangChain’s `VectorStoreRetrieverMemory`
- Store structured Q&A facts or timelines
- Indexed long-term memory support

---

### 📁 PHASE 4: Document Q&A + Chunk Tracking

Enhance document summarization:

- 🔍 Show exactly which **chunks** from the PDF were used in the answer
- 📄 Highlight matching text in context
- 🗂️ Support multi-PDF ingestion with separate memory per doc

---

### 🤖 PHASE 5: Tool-Using Assistant API

Turn this logic into a **production API backend**:

- 🔌 Framework: `FastAPI` or `Litestar`
- 🧠 Endpoint: `/ask` → returns final answer + trace
- 💬 Useful for building your own chatbot or research SaaS

---

### 🌐 PHASE 6: Assistant with Browsing + Plugin Tools

Make the agent smarter at real-world decisions:

- 🌐 Use LangGraph or LCEL to handle branching logic
- 🤖 Tools like:
  - `YouTubeTranscriptTool`
  - `Google Scholar Reader`
  - `News Aggregator`
- 🧠 Agent decides:
  - Should I search?
  - Should I summarize?
  - Can I skip?

---

> ⭐ Want to contribute to any phase? Fork the repo, build a feature, and submit a PR! The roadmap is open for collaboration.

---

```

Let me know if you want:
- `LICENSE` file (MIT version)
- A matching `.env.example` file
- `demo/screenshot.png` placeholder
- `contributing.md` file

All of this helps boost your open-source visibility!
```



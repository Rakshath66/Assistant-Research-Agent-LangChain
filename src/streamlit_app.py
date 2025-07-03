# Streamlit UI for PDF + Web + Calculator Agent
# app.py

import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from agent_tools import make_all_tools  # ✅ custom tools
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
api_key = os.getenv("OPENAI_API_KEY")

# ✅ Set required env var
os.environ["OPENAI_API_KEY"] = api_key
# api_key = os.environ.get("OPENAI_API_KEY") DEPLOYMENT

# ✅ Set up LLM
headers = {
    "Authorization": f"Bearer {api_key}",             # ✅ Mandatory
    "HTTP-Referer": "https://github.com/Rakshath66",  # ✅ Required by OpenAI
    "X-Title": "LangChain Agent"                      # ✅ Optional, branding
}
llm = ChatOpenAI(   
    base_url="https://openrouter.ai/api/v1",
    model="mistralai/mistral-7b-instruct",
    temperature=0,
    default_headers=headers
)
# ✅ Memory to remember past queries
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

tools = make_all_tools(llm)

# ✅ Agent that uses tools + memory
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, #FORCE TO USE TOOLS
    memory=memory,
    handle_parsing_errors=True,
    verbose=True,
    return_intermediate_steps=True  # ✅ REQUIRED!
)

# Wrap it to enforce chain-of-thought
from datetime import datetime
class SmartAgent:
    def __init__(self, agent):
        self.agent = agent

    def ask(self, question):
        current_year = datetime.now().year
        prompt = (
            f"{question}\n\n"
            f"Break this into steps. Search if needed. Use calculator tool for any math. Use {current_year} if today's date is required."
            f"If PDFs are available, use summarize_pdf to extract insights.If the info is not in the PDF, try summarize_wikipedia or web search."
        )
        return self.agent.invoke({"input": prompt})

smart_agent = SmartAgent(agent)

# ✅ Streamlit UI
st.set_page_config(page_title="🧠 PDF + Web RAG Agent") # layout="wide"

#red, #ff7f7f, red
##1ca9e0, #c2f0ff, #1ca9e0 - blue
# 🎨 Title with gradient
st.markdown(
    """
    <h1 style="
        background: linear-gradient(to right, #1ca9e0, #c2f0ff, #1ca9e0);
        -webkit-background-clip: text;
        color: transparent;
        font-size: 3rem;
        text-align: center;
        padding: 1rem 0;
    ">
        🔎 Assistant Research Agent
    </h1>
    
    """,
    unsafe_allow_html=True
)

# 📁 Sidebar: Upload PDF
st.sidebar.header("📄 Upload PDF")
pdf_files = st.sidebar.file_uploader("Upload PDFs to analyze", type="pdf", accept_multiple_files=True)

pdf_paths = []
if pdf_files:
    for pdf in pdf_files:
        path = f"uploaded_{pdf.name}"
        with open(path, "wb") as f:
            f.write(pdf.read())
        pdf_paths.append(path)
    st.sidebar.success(f"Uploaded {len(pdf_paths)} PDFs ✅")

# 💬 Chat Interface
st.markdown("""<h3 style="text-align: center;">🤖 Ask Anything</h>""", unsafe_allow_html=True)
# query = st.text_input("Type your question:")
with st.form(key="chat_form", clear_on_submit=True):
    query = st.text_input("Type your question:")
    submit = st.form_submit_button("📤 Send", use_container_width=True)


if submit and query:
    # Inject the PDF path into query if PDF exists
    if pdf_paths:
        query += f"\n\nUse summarize_pdf({repr(pdf_paths)}) to analyze the uploaded PDFs."


    with st.spinner("Thinking..."):
        response = smart_agent.ask(query)
        st.markdown("#### 💡 Answer:")
        st.success(response["output"] if isinstance(response, dict) else response)
        # ✅ Show final answer
        # ✅ Warn if no external context (PDF/Web) used
        used_tools = {step[0].tool for step in response.get("intermediate_steps", [])}
        used = {t.lower() for t in used_tools}
        contextual_tools = {"summarize_pdf", "tavily_search_results_json", "summarize_wikipedia"}

        with st.expander("⚠️ &nbsp;  How to Use This AI Agent &nbsp;  ⚠️ ", expanded=False):
            st.markdown("""
            **🧠 Assistant Researcher** is a multi-tool AI agent built using LangChain + RAG.

            It uses tools like:
            - 📄 `summarize_pdf` to read PDFs
            - 🌐 `tavily_search_results_json` to search the Web
            - 🧮 `Calculator` to solve math
            - 📚 `wikipedia` for quick facts
            - 🔁 `reverse_tool` to reverse
            - 💡 `memory` for past info

            ---
            ### ✅ Example Questions:
            - *"What projects did Rakshath work on in the given pdf rakshath.pdf?"*
            - *"How many years ago was Narendra Modi born and square that number?"*

            ---
            ### ⚠️ Notes:
            - May make mistakes if facts are unclear or tools fail - Give clear prompt.
            - Avoid vague inputs like “What do you think?” – be specific!
            - If PDF is not uploaded or tools not used, results may be limited.

            ---
            💡 *Tip: This agent thinks step-by-step (Chain-of-Thought). Scroll below to see how it reasoned.*
            """)

        if not used & contextual_tools:
            st.warning("⚠️ No relevant context found from Web or documents. The answer may be limited and only be based only on the model's memory.")

        # chatgpt show unique tools used here

        # ✅ Show full reasoning like Thoughts → Actions → Results
    if "intermediate_steps" in response:
        st.markdown("### 🧠 See How Researcher is Thinking? - Reasoning Trace")

        used_tools_set = set()

        for action, observation in response["intermediate_steps"]:
            # 🧼 Skip noisy errors
            if action.tool == "_Exception" or "Invalid Format" in str(observation):
                continue

            import re
            log = getattr(action, "log", "")
            # Remove lines that start with 'Action:' or 'Action Input:'
            thought = "\n".join(
                line for line in log.splitlines() 
                if not re.match(r"^Action(\sInput)?:", line)
            ).strip()

            tool_name = action.tool
            tool_input = action.tool_input
            result = str(observation)
            used_tools_set.add(tool_name)

            # Short preview or collapsible full result
            short_result = result[:300] + "..." if len(result) > 300 else result
            
            # ff9900 - orange
            st.markdown(f"""
            <div style="padding: 10px; padding-bottom:1px; border-left: 4px solid #1ca9e0; background-color: black; color: white">
                <b>🤔 Thought:</b> <br>{thought}<br><br>
                <b>⚙️ Action:</b> <br>{tool_name}<br><br>
                <b>📥 Input:</b> <br><code>{tool_input}</code><br><br>
            </div>
            """, unsafe_allow_html=True)

            if len(result) > 300:
                with st.expander("📤 Result (click to expand)"):
                    st.markdown(result)
            else:
                st.markdown(f"📤 **Result:** {short_result}")

        # ✅ Show unique tools used
        if used_tools_set:
            st.markdown("#### 🛠️ Tools Used:")
            all_tool_names = {
                "summarize_pdf": "📄 Summarize PDF",
                "tavily_search_results_json": "🌐 Web Search",
                "Calculator": "🧮 Calculator",
                "python_repl": "🧮 Calculator",
                "summarize_wikipedia": "📚 Wikipedia",
                "reverse_tool": "🔁 Reverse Text"
            }
            
            #orange
            tool_list_html = "<div style='background-color: #111; padding: 15px; border-radius: 10px;'>"
            tool_list_html += "<h4 style='color: #1ca9e0;'>&nbsp;&nbsp;📝 Checklist</h4><ul style='list-style: none; padding-left: 0;'>"

            for tool, label in all_tool_names.items():
                tool_key = tool.lower()
                status = "✅ Used" if tool_key in {t.lower() for t in used_tools_set} else "❌ Not Used"
                color = "green" if tool in used_tools_set else "grey"
                tool_list_html += f"<li style='color:{color}; font-size: 16px;'>{status} - {label}</li>"

            tool_list_html += "</ul></div>"
            st.markdown(tool_list_html, unsafe_allow_html=True)

if not submit:
    with st.expander("⚠️ &nbsp;  How to Use This AI Agent &nbsp;  ⚠️ ", expanded=False):
        st.markdown("""
        **🧠 Assistant Researcher** is a multi-tool AI agent built using LangChain + RAG.

        It uses tools like:
        - 📄 `summarize_pdf` to read PDFs
        - 🌐 `tavily_search_results_json` to search the Web
        - 🧮 `Calculator` to solve math
        - 📚 `wikipedia` for quick facts
        - 🔁 `reverse_tool` to reverse
        - 💡 `memory` for past info

        ---
        ### ✅ Example Questions:
        - *"What projects did Rakshath work on in the given pdf rakshath.pdf?"*
        - *"How many years ago was Elon Musk born and square that number?"*

        ---
        ### ⚠️ Notes:
        - May make mistakes if facts are unclear or tools fail - Give clear prompt.
        - Avoid vague inputs like “What do you think?” – be specific!
        - If PDF is not uploaded or tools not used, results may be limited.

        ---
        💡 *Tip: This agent thinks step-by-step (Chain-of-Thought). Scroll below to see how it reasoned.*
        """)

# ✅ Example use case suggestion
st.markdown("""
<div style="margin-top:20px; padding: 10px; border: 1px dashed #aaa;">
    <strong>🧪 Try asking:</strong><br>
    <code>Who is the founder of Tesla? calculate the number of letters in their last name.</code><br>
    <em>→ If PDF is uploaded, It'll read the PDF and extract info automatically!</em>
</div>
""", unsafe_allow_html=True)

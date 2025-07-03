# agent_tools.py

from langchain.tools import tool, Tool
from langchain.utilities import WikipediaAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import Tool
from langchain_experimental.tools.python.tool import PythonREPLTool # LangChain already provides a simple Python REPL tool that lets the agent do math.
import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain_core.runnables import RunnableLambda
import ast

# ✅ 1. Reverse Tool
@tool
def reverse_tool(input_str: str) -> str:
    """Reverses the given string."""
    return input_str[::-1]

# ✅ 2. Wikipedia Summary Tool
@tool
def summarize_wikipedia(topic: str) -> str:
    """Searches Wikipedia for a topic and summarizes it."""
    return WikipediaAPIWrapper().run(topic)

# ✅ 3. PDF Summary Tool
def summarize_pdf(pdf_input: list, llm) -> str:
    try:
        # ✅ Safely parse stringified list to real list
        if isinstance(pdf_input, str):
            pdf_input = ast.literal_eval(pdf_input.strip())

        if isinstance(pdf_input, str):
            pdf_input = [pdf_input]  # Single file fallback

        all_text = ""
        for path in pdf_input:
            if not os.path.exists(path):
                return f"Error: File not found -> {path}"
            doc = fitz.open(path)
            for page in doc:
                all_text += page.get_text()
            doc.close()

        return llm.invoke(f"Summarize the following text:\n\n{all_text[:3000]}")
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

# ✅ 4. Tavily Web Search Tool
search_tool = TavilySearchResults(max_results=5)

# ✅ 5. Calculator Tool
calculator_tool = PythonREPLTool(name="Calculator", description="Useful for math or conversions.")

# ✅ 6. Collect All Tools
def make_all_tools(llm):
    return [
        Tool(
            name="summarize_pdf",
            func=lambda path: summarize_pdf(path, llm),
            description="Summarizes content from uploaded PDF file paths. Only works with **local file paths**. Do not use on URLs or search results.",
        ),
        summarize_wikipedia,
        reverse_tool,
        search_tool,
        calculator_tool
    ]

# all_tools = [
#     summarize_wikipedia,
#     summarize_pdf,
#     reverse_tool,
#     search_tool,
#     calculator_tool
# ]

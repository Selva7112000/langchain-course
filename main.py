from dotenv import load_dotenv
load_dotenv()
import os

from langchain.agents import create_agent 
from langchain.tools import tool
from langchain_core.messages import HumanMessage 
from langchain_ollama import ChatOllama 
from langchain_tavily import TavilySearch
# from tavily import TavilyClient

# tavily = TavilyClient()

# @tool 
# def search(query: str) -> str:
#     """
#     Tool that searches over internet 
#     Args:
#         query: The query to search for 
#     Returns:
#         The search result
#     """
#     print(f"Searching for: {query}")
#     return tavily.search(query=query)


llm = ChatOllama(temperature=0, model="llama3.1")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bangalore(bengaluru) on linkedIn and Naukri")]})
    print(result)


if __name__ == "__main__":
    main()

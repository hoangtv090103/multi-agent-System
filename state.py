from typing import TypedDict, List
from langgraph.graph import StateGraph, END

class AgentState(TypedDict):
    topic: str
    research_data: List[str] # A list of findings 
    blog_post: str # The final output

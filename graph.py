from agents import research_node, write_node
from state import AgentState
from langgraph.graph import StateGraph, END


workflow = StateGraph(AgentState)
workflow.add_node("Researcher", research_node)
workflow.add_node("Writer", write_node)

# Flow: Start -> Researcher -> Writer -> END
workflow.set_entry_point("Researcher")
workflow.add_edge("Researcher", "Writer")
workflow.add_edge("Writer", END)

app = workflow.compile()
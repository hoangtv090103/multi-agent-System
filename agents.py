from langchain_community.tools.ddg_search import DuckDuckGoSearchRun

from state import AgentState

def research_node(state: AgentState):
    topic = state.get("topic", "")
    print(f"Researcher is looking up: {topic}...")

    search = DuckDuckGoSearchRun()

    try:
        results = search.run(f"key facts and latest news about {topic}")
    except Exception as e:
        results = f"Could not find data: {e}"

    print("Research complete.")

    return {
        "research_data": state.get("research_data", []) | [results]
    }



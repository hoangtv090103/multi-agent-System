from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
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


def write_node(state: AgentState):
    print("Writer is drafting the post...")

    topic = state.get("topic", "")
    data = state["research_data"][-1] if state["research_data"] else ""

    llm = ChatOllama(model="granite4:tiny-h", temperature=0.7)

    prompt = ChatPromptTemplate.from_template(
        """You are a tech blog writer. 
Write a short, engaging blog post about "{topic}" 
based ONLY on the following research data:

{data}

Return just the blog post content."""
    )

    chain = prompt | llm
    response = chain.invoke(
        {
            "topic": topic,
            "data": data
        }
    )

    print("Writing complete.")
    return {
        "blog_post": response.content
    }
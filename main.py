from graph import app
from state import AgentState


if __name__ == "__main__":
    print("Starting the Multi-Agent System...\n")

    inputs: AgentState = {
        "topic": input("Enter the topic you want to research"),
        "research_data": [],
        "blog_post": "",
    }

    result = app.invoke(inputs)
    print("\n---------------- FINAL OUTPUT ----------------\n")
    print(result["blog_post"])
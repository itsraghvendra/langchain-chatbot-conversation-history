
import os
from dotenv import load_dotenv

load_dotenv()  # Read API settings from the local .env file
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq


# Keep only the most recent messages. An even number helps preserve user/AI pairs.
MAX_HISTORY_MESSAGES = 10

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly, accurate educational Q&A assistant. "
               "Use earlier conversation when it helps. Keep answers simple. "
               "If you do not know something, say so."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])


def trim_history(history, max_messages=MAX_HISTORY_MESSAGES):
    """Return only the newest messages while keeping the list within the limit."""
    if len(history) <= max_messages:
        return history
    return history[-max_messages:]


def main():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("Missing GROQ_API_KEY.")
        print("Set your Groq API key first. See README.md for easy instructions.")
        return

    # Use a current Groq chat model.
    llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)
    chain = prompt | llm
    history = []

    print("\n=== Simple LangChain Chatbot ===")
    print("Ask a question. Type 'exit' to stop.\n")

    while True:
        question = input("You: ").strip()
        if question.lower() in {"exit", "quit"}:
            print("Chatbot: Goodbye!")
            break
        if not question:
            continue

        try:
            # Send prior turns to the model.
            response = chain.invoke({
                "chat_history": trim_history(history),
                "question": question
            })
            answer = response.content
            print(f"Chatbot: {answer}\n")

            # Store both sides of the interaction.
            history.append(HumanMessage(content=question))
            history.append(AIMessage(content=str(answer)))
            history = trim_history(history)
        except Exception as error:
            print("Sorry, something went wrong. Check your internet/API key/model.")
            print(f"Details: {error}\n")


if __name__ == "__main__":
    main()

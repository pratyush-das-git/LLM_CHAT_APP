from memory.chat_memory import ChatMemory
from llm.chat_service import get_ai_response
from config.settings import settings 
from utils.logger import get_logger

logger=get_logger()

def main():
    print("\n Welcome to the AI Chatbot! Type 'exit' to quit.\n")

    memory=ChatMemory(settings.MAX_HISTORY)

    while True:
        user_input=input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        ai_response=get_ai_response(memory,user_input)
        print(f"AI: {ai_response}\n")

if __name__ == "__main__":
    main()
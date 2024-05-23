import openai
from prompts import generate_response

# Set your OpenAI API key
openai.api_key = 'your-api-key-here'

def main():
    conversation_history = []

    print("Chatbot: Hello, how can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        
        response = generate_response(user_input, conversation_history)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()

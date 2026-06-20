def get_response(user_input):
    message = user_input.lower().strip()

    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! How can I help you?",
        "hey": "Hey! Nice to meet you.",
        "how are you": "I'm doing great, thank you for asking!",
        "what is your name": "My name is CodeAlpha Chatbot.",
        "who are you": "I am a simple rule-based chatbot built with Python.",
        "what can you do": "I can answer a few basic questions and chat with you.",
        "bye": "Goodbye! Have a nice day.",
    }

    return responses.get(message, "Sorry, I don't understand that. Please try another message.")


def main():
    print("CodeAlpha Chatbot")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Bot: {response}")

        if user_input.lower().strip() == "bye":
            break


if __name__ == "__main__":
    main()

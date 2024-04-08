# Simple chatbot
print("Chatbot: Hi there! I'm a simple chatbot. How can I assist you today?")
while True:
    user_input = input("You: ").lower()
    
    if "hello" in user_input:
        print("Chatbot: Hello! How can I help you?")
    elif "how are you" in user_input:
        print("Chatbot: I'm just a computer program, so I don't have feelings, but thanks for asking!")
    elif "bye" in user_input:
        print("Chatbot: Goodbye! Have a great day!")
        break
    else:
        print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")

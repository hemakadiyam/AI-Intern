def chatbot_response(user_input):
    user_input = user_input.lower() 
    if "hello" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but thanks for asking! How can I assist you?"
    elif "your name" in user_input:
        return "I'm a simple rule-based chatbot created to assist you!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rhephrase?"
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
    if "bye" in user_input.lower():
        break

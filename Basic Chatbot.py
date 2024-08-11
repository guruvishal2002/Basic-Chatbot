# Basic Chatbot

# Create a text-based chatbot that can have
# conversations with users. You can use natural
# language processing libraries like NLTK or spaCy to
# make your chatbot more conversational.

import random

def greet():
    responses = ["Hi there! How can I assist you today?", "Hello! What can I do for you?", "Hey! How's it going?", "Greetings! How can I help?"]
    return random.choice(responses)

def farewell():
    responses = ["Catch you later!", "Until next time!", "Take care!", "See you soon!"]
    return random.choice(responses)

def chatbot_response(user_input):
    input = input.lower()
    
    if input in ["hi", "hello", "hey", "greetings"]:
        return greet()
    
    elif input in ["what's your name", "who are you", "name"]:
        return "I'm Chatbot, your assistant. How can I help you?"
    
    elif input in ["how are you", "what's up", "how's it going"]:
        return "I'm doing great, thanks for asking! What about you?"
    
    elif input in ["sorry", "apologies", "my bad"]:
        return "No problem at all. How can I assist you further?"
    
    elif input in ["bye", "goodbye", "see you later", "take care"]:
        return farewell()
    
    else:
        return "I'm not sure how to respond to that. Perhaps try asking something else or check online."

def chat():
    print("Welcome to the Chatbot!")
    print("Feel free to start a conversation, or type 'bye' to exit.")

    while True:
        input = input("You: ")
        if input.lower() in ['bye', 'goodbye', 'see you later', 'take care']:
            print("Chatbot: ", chatbot_response(input))
            break
        else:
            print("Chatbot: ", chatbot_response(input))

if __name__ == "__main__":
    chat()

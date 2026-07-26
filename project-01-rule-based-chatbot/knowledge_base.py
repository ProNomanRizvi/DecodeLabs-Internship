# knowledge_base.py
# This file only stores data - no logic here.
# Each key is a user message, each value is the bot's reply.

responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! Nice to see you.",
    "how are you": "I'm doing great, thanks for asking!",
    "what is your name": "I am a simple rule-based chatbot.",
    "help": "You can talk to me using simple greetings. Type 'bye' to exit.",
    "bye": "Goodbye! Have a nice day."
}

# Message shown when input does not match any key above
fallback_message = "Sorry, I did not understand that."
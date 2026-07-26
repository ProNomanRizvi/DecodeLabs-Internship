# chatbot.py
# Main chatbot logic.
# Follows Input -> Process -> Output loop until user exits.

from knowledge_base import responses, fallback_message


def get_reply(user_input):
    # Look up the input in our dictionary.
    # If not found, use the fallback message instead.
    return responses.get(user_input, fallback_message)

def main():
    print("Chatbot is running. Type 'bye' to exit.")

    while True:
        # Get raw input from user
        raw_input = input("You: ")

        # Clean the input: lowercase and remove extra spaces
        clean_input = raw_input.lower().strip()

        # Get the bot's reply
        reply = get_reply(clean_input)
        print("Bot:", reply)

        # Exit the loop if user typed 'bye'
        if clean_input == "bye":
            break


if __name__ == "__main__":
    main()
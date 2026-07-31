# Project 1: Rule-Based AI Chatbot

A simple chatbot that replies to fixed user inputs using a dictionary lookup.

## Why this project exists

Before working with machine learning models that make probabilistic decisions, this project builds the foundation: a deterministic system where every input maps to a known, traceable output. It's the "white box" counterpart to the "black box" models that come later in this internship — no hidden reasoning, no randomness, just clear input-to-output logic.

## What it does

- Takes user input in a loop
- Cleans the input (lowercase, remove extra spaces)
- Looks up a matching response in a dictionary
- Shows a fallback message if no match is found
- Exits when user types "bye"

## Demo
```
Chatbot is running. Type 'bye' to exit.
You: hello
Bot: Hi there! How can I help you?
You: help
Bot: You can talk to me using simple greetings. Type 'bye' to exit.
You: bye
Bot: Goodbye! Have a nice day.
```
## Files

- `knowledge_base.py` - stores all responses as a dictionary
- `chatbot.py` - main chatbot loop and logic
- `tests/test_chatbot.py` - automated tests for the reply logic

## How to run

```bash
python3 chatbot.py
```

## How to run tests

```bash
pip install -r requirements.txt
python3 -m pytest tests/ -v
```

## Key concept

Uses `dictionary.get(key, fallback)` instead of a long if-elif chain.
This is faster (constant time lookup) and easier to maintain.

## Key decision

An if-elif chain would have worked too, but it scales linearly — every new response means checking one more condition before the fallback. A dictionary lookup stays constant time no matter how many responses get added later.
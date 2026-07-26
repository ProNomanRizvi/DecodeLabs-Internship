# Project 1: Rule-Based AI Chatbot

A simple chatbot that replies to fixed user inputs using a dictionary lookup.

## What it does

- Takes user input in a loop
- Cleans the input (lowercase, remove extra spaces)
- Looks up a matching response in a dictionary
- Shows a fallback message if no match is found
- Exits when user types "bye"

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
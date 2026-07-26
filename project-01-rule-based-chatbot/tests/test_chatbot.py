# tests/test_chatbot.py
# Simple tests for the chatbot's get_reply function.
# Run with: python3 -m pytest tests/

import sys
import os

# Add parent folder to path so we can import chatbot.py
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from chatbot import get_reply


def test_known_greeting():
    # "hello" should return the greeting response
    assert get_reply("hello") == "Hi there! How can I help you?"


def test_known_bye():
    # "bye" should return the goodbye response
    assert get_reply("bye") == "Goodbye! Have a nice day."


def test_unknown_input():
    # Random text not in dictionary should return fallback message
    assert get_reply("random text here") == "Sorry, I did not understand that."


def test_case_sensitivity():
    # get_reply expects already-cleaned (lowercase) input
    # so uppercase input should NOT match and should return fallback
    assert get_reply("HELLO") == "Sorry, I did not understand that."
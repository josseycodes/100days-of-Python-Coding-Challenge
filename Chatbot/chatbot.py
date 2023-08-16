import nltk
import random
from nltk.chat.util import Chat, reflections

# Define chatbot responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you?",]
    ],
    [
        r"(.*) (location|city) ?",
        ["Columbus is a great city in Ohio.",]
    ],
    [
        r"how (are you|are you doing)?",
        ["I'm doing well, thank you!", "I'm just a chatbot, but I'm here to help!",]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I can help you with that.",]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "See you later!",]
    ],
]

# Create a chatbot
def chatbot():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download("punkt")  # Download NLTK data if not already downloaded
    chatbot()

import random
from textblob import TextBlob

print("Hello! I am your AI chatbot. Type 'bye' to exit.")

# Predefined responses
greetings = ["hello", "hi", "hey"]
greeting_responses = ["Hi there!", "Hello!", "Hey! How can I help you?"]

how_are_you_responses = [
    "I'm doing great!",
    "All good here 😊",
    "Running smoothly!"
]

help_responses = [
    "I can chat with you 😊",
    "Try asking me about your day!",
    "I'm here to talk!"
]
name = ""

while True:
    user_input = input("You: ").lower()

    # Sentiment analysis
    polarity = TextBlob(user_input).sentiment.polarity

    if user_input == "bye":
        print("Bot: Goodbye! 👋")
        break

    elif any(word in user_input for word in greetings):
        print("Bot:", random.choice(greeting_responses))

    elif "how are you" in user_input:
        print("Bot:", random.choice(how_are_you_responses))

    elif "help" in user_input:
        print("Bot:", random.choice(help_responses))

    elif "your name" in user_input:
        print("Bot: I'm your AI chatbot 🤖")

    else:
        # Smart fallback using sentiment
        if polarity > 0:
            print("Bot: That sounds really nice! 😊 Tell me more.")
        elif polarity < 0:
            print("Bot: I'm sorry to hear that 😔 Want to talk about it?")
        else:
            print("Bot: Interesting... tell me more!")
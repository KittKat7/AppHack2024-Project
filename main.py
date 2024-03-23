import random
import pyttsx3
from query import *
import threading

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',250)  # Set the rate of speech (words per minute)
engine.setProperty('voices', voices[0].id)  # Index 1 usually corresponds to a female voice

# Define a function to greet the user
def greet():
    greetings = ["Hello!", "Hi there!", "Hey!"]
    greet_msg = random.choice(greetings)
    print(greet_msg)
    speak(greet_msg)

# Define a function to speak
def speak(message):
    engine.say(message)
    engine.runAndWait()


# Define a function to take user input and respond accordingly
def respond_to_user_input(user_input):
    response = query(user_input)
    print(response)
    speak(response)
    return

# Main function to run the virtual assistant
def main():
    greet()
    while True:
        user_input = input("You: ").lower()
        end_chat = respond_to_user_input(user_input)
        if end_chat:
            break

if __name__ == "__main__":
    main()

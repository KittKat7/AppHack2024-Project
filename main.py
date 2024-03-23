import random
import pyttsx3
import time

engine = pyttsx3.init()
def speak(message):
    engine.say(message)
    engine.runAndWait()
def greet():
    greetings = ["Hello!", "Hi there!", "Hey!"]
    greet_msg = random.choice(greetings)
    print(greet_msg)
    speak(greet_msg)

def respond_to_user_input(user_input):
    if "how are you" in user_input:
        response="Im just a boy living in a lon"
        print(response)
        speak(response)
    elif "bye" in user_input:
        response="BYEEEEEE BITCH"
        print(response)
        speak(response)
        time(50)
        return True
    else:
        response="you stupid"
        print(response)
        speak(response)

def main():
    greet()
    while True:
        user_input = input("You: ").lower()
        end_chat = respond_to_user_input(user_input)
        if end_chat:
            break

if __name__ == "__main__":
    main()

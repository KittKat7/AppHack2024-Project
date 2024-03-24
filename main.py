import random
import sys
import os
from query import *
import globals as globals

if "--cli" in sys.argv:
    sys.argv.append("--cli-in")
    sys.argv.append("--cli-out")
    sys.argv.remove("--cli")

speechout = True
if "--cli-out" in sys.argv:
    speechout = False
    sys.argv.remove("--cli-out")
else:
    from texttospeach import *
speechin = True
if "--cli-in" in sys.argv:
    speechin = False
    sys.argv.remove("--cli-in")
else:
    import microphone

if "--force-api" in sys.argv:
    globals.force_api_usage = True
    sys.argv.remove("--force-api")
    print("FORCING API")
else:
    globals.force_api_usage = False


def getSpeachInput():
    return microphone.mic().getSpeach()

def passiveListen(wakeWord):
    microphone.mic().passiveListen(wakeWord)

def output(text):
    print("Nebula:\t" + text)
    if speechout:
        speak(text)


# Define a function to greet the user
def greet():
    greetings = ["Hi there!", "Hey!", "Good morning!", "Good afternoon!",
                 "Greetings!", "Howdy!", "What's up?", "Yo!", "Hiya!", "Salutations!",
                 "Well met!", "Hello there!", "Yer", "What's new?", "Bonjour!", "Ciao!"]
    greet_msg = random.choice(greetings)
    output(greet_msg)


# Define a function to take user input and respond accordingly
def respond_to_user_input(user_input):
    response = query(user_input)
    output(response)
    return

def get_input():
    if speechin:
        passiveListen("Nebula")
        output("yes?")
        user_input = getSpeachInput().lower()
        print(f"You: {user_input}")
        #gets prompt
        return user_input
    else:
        return input("Prompt: ").lower()

# Main function to run the virtual assistant
def main():
    greet()
    while True:
        #waits for wake up
        user_input = get_input()

        #user_input = input("You:\t").lower()
        respond_to_user_input(user_input)


if __name__ == "__main__":
    main()

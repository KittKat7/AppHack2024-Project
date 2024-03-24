import random
import sys
import microphone
import os

from query import *

speechmode = True
if "--cli" in sys.argv:
    speechmode = False
else:
    from texttospeach import *

def getSpeachInput():
    return microphone.mic().getSpeach()

def passiveListen(wakeWord):
    microphone.mic().passiveListen(wakeWord)

def output(text):
    print("Nebula:\t" + text)
    if speechmode:
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


# Main function to run the virtual assistant
def main():
    greet()
    while True:
        #waits for wake up
        passiveListen("Nebula")
        output("yes?")

        #gets prompt
        user_input = getSpeachInput().lower()
        print(user_input)

        #user_input = input("You:\t").lower()
        respond_to_user_input(user_input)


if __name__ == "__main__":
    main()

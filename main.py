import random
import sys

from query import *

speechmode=True
if "--cli" in  sys.argv:
    speechmode=False
else:
    from texttospeach import *

def output(text):
    print(text)
    if speechmode:
        speak(text)
# Define a function to greet the user
def greet():
    greetings = ["Hi there!", "Hey!", "Good morning!","Good afternoon!",
"Greetings!","Howdy!","What's up?","Yo!","Hiya!","Salutations!","How's it going?",
"Well met!","Hi, how are you?","Hello there!","Hey, what's happening?","How are you doing?",
"What's new?","Hi, how's your day?"]
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
        user_input = input("You: ").lower()
        respond_to_user_input(user_input)


if __name__ == "__main__":
    main()

import random
import pyttsx3
import threading

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
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
    # You can add more responses based on user input
    if "how are you" in user_input:
        response = "I'm just a program, but I'm functioning well! How can I assist you?"
        print(response)
        speak(response)
    elif "bye" in user_input:
        response = "Goodbye!"
        print(response)
        speak(response)
        return True  # Return True to indicate the conversation should end
    else:
        response = "I'm not sure how to respond to that. Can you ask me something else?"
        print(response)
        speak(response)

# Main function to run the virtual assistant
def main():
    greet()
    in_nebula_state = False
    while True:
        user_input = input("You: ").lower()
        if in_nebula_state:
            if user_input.strip() == "nebula":
                in_nebula_state = False
                response = "Welcome back!"
                print(response)
                speak(response)
        else:
            end_chat = respond_to_user_input(user_input)
            if end_chat:
                in_nebula_state = True

if __name__ == "__main__":
    main()

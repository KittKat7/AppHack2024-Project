import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',250)  # Set the rate of speech (words per minute)
engine.setProperty('voices', voices[0].id)  # Index 1 usually corresponds to a female voice


# Define a function to speak
def speak(message):
    engine.say(message)
    engine.runAndWait()


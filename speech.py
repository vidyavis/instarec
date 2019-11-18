# importing the pyttsx library
import pyttsx3

# initialisation
engine = pyttsx3.init()

# testing
def voice(text):

    engine.say(text+"Detected")
    engine.runAndWait()

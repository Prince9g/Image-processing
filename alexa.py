import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime
# Initialize the speech recognizer
listener = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to speak out the text
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for commands
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')  # Indicate that the program is listening
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print('Command:', command)  # Print the recognized command
            return command
    except Exception as e:
        print(e)  # Print any exceptions that occur

# Main function to execute commands
def run_prince():
    command = take_command()
    if command:
        if 'play' in command:
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)

        elif 'hey' in command:
            talk('hey, master')    
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who the heck is' in command:
            person = command.replace("who the heck is", '')
            info = wikipedia.summary(person, 1)
            print('Information:', info)  # Print the retrieved information
            talk(info)
        elif 'date' in command:
            talk('Sorry, I have a headache')  # A humorous response
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')  # Another humorous response
        elif 'joke' in command:
            talk(pyjokes.get_joke())  # Tell a joke
        else:
            talk('Please say the command again.')  # Ask the user to repeat if command not recognized
    else:
        talk("Sorry, I couldn't understand. Please try again.")  # Prompt user to try again

# Continuous loop to keep the program running
while True:
    run_prince()

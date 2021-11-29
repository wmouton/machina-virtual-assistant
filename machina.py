import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f3')
engine.say('Hello, I am Machina, your personal virtual assistant.')
engine.say('What can I do for you?.')
engine.runAndWait()
try:
  with sr.Microphone() as source:
    print('listening...')
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
    command = command.lowser()
    if 'Machina' in command:

      print(command)

except:
    pass
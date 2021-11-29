import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f3')

def talk(text):
  engine.say(text)
  engine.runAndWait()

def take_command():
  try:
    with sr.Microphone() as source:
      talk('Hi, I am machina, created by mister W Mooton, how may I be of service?')
      print('listening...')
      voice = listener.listen(source)
      command = listener.recognize_google(voice)
      command = command.lower()
      if 'machina' in command:
        command = command.replace('machina', '')
        print(command)
  except:
    pass
  # return command

def run_machina():
  command = take_command()
  print(command)
  if 'play' in command:
    song = command.replace('play', '')
    talk('playing ' + song)
    pywhatkit.playonyt(song)
  elif 'time' in command:
    time = datetime.datetime.now().strftime('%I:%M %p')
    print(time)
    talk('The current time is ' + time)
  elif 'who is' in command:
    person = command.replace('who is', '')
    info = wikipedia.summary(person, 1)
    print(info)
    talk(info)
  elif 'date' in command:
    talk('sorry, I have a headache')
  elif 'are you single' in command:
    talk('I am in a relationship with wifi')
  elif 'joke' in command:
    talk(pyjokes.get_joke(language="en", category="neutral"))
  else:
    talk('Please say the command again.')

while True:
  run_machina()
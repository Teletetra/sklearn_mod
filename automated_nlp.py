import speech_recognition as sr
import pyttsx3 as pt

listener=sr.Recognizer()
engine=pt.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voice[1].id)
deftalk(text):
    engine.say("i am your kanishk")
    engine.say("what can i do for you")
    engine.runAndWait()
    

while True:
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "kanishk" in command:
                
                engine.say(command)
                talk(command)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))  

import speech_recognition as sr 
import pyttsx3 

start = pyttsx3.init()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("скажи что-нибудь")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
        try: 
            task = r.recognize_google(audio, language="ru-RU").lower()
            print(task)
        except:
            task = listen()
        return task
def request(task):
    if "пока" in task:
        text = "прощай"
        start.say(text)
        start.runAndWait()
while True:
    request(listen())            


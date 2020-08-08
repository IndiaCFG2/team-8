import speech_recognition as sr
from googletrans import Translator

filename = "hindi.wav"

r = sr.Recognizer()
translator = Translator()

with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data,language='hi-IN')
    print(text)

result = translator.translate(text, src='hi', dest='en')
print(result.text)

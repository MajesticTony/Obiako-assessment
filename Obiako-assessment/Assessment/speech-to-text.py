import speech_recognition as sr
r = sr.Recognizer()

harvard = sr.AudioFile('Good morning.wav')
with harvard as source:
    audio = r.record(source, duration=4)

type(audio)
r.recognize_google(audio)

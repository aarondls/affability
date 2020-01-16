import speech_recognition as speechrecog
import subprocess

recog = speechrecog.Recognizer()
mic = speechrecog.Microphone()

# print ("initialized speech recognition")

def reply(response):
    subprocess.call(['say', response])

# reply("voice response initialized")

print("ready")

''' with mic as source:
    print("say something!")
    recog.adjust_for_ambient_noise(source)
    audio = recog.listen(source)
    text = recog.recognize_google(audio)
    #reply(text) '''

text = input()

if "hello" in text:
    print("hello")
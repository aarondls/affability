import speech_recognition as speechrecog
import subprocess
import DialogflowAPITest 

recog = speechrecog.Recognizer()
mic = speechrecog.Microphone()

print ("initialized speech recognition")

def reply(response):
    subprocess.call(['say', response])

print ("voice response initialized")

print("ready")

''' with mic as source:
    print("say something!")
    recog.adjust_for_ambient_noise(source)
    audio = recog.listen(source)
    text = recog.recognize_google(audio)
    reply("Wait a second") '''

text = input()
# print("your response is "+text)
# if "hello" in text:
    # print("hello")

DialogflowAPITest.askBotResponse(text)
reply(DialogflowAPITest.response.query_result.query_text)
reply("I am" + DialogflowAPITest.response.query_result.intent.display_name + "percent sure of your intent")
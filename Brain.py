import speech_recognition as speechrecog
import subprocess
import DialogflowAPITest 

recog = speechrecog.Recognizer()
mic = speechrecog.Microphone()

def reply(response):
    subprocess.call(['say', response])

''' with mic as source:
    print("say something!")
    recog.adjust_for_ambient_noise(source)
    audio = recog.listen(source)
    text = recog.recognize_google(audio)
    reply("Wait a second") '''

if __name__ == '__main__':
    print("ready")
    text = input()
    DialogflowAPITest.askBotResponse(text)
    ''' print(DialogflowAPITest.reply)
    print(DialogflowAPITest.detectedIntent)
    print(DialogflowAPITest.confidence)
    print(DialogflowAPITest.requiredParametersPresent)'''
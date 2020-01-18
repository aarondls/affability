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

def alarm():
    # detected intent is alarm and perform necessary tasks here
    print("alarm function called")

functions = {
    "Alarm": alarm
}

keepGoing = True

if __name__ == '__main__':
    print("ready")
    while keepGoing == True:
        text = input()
        if text == "End":
            keepGoing = False
            break
        else:
            DialogflowAPITest.askBotResponse(text)
            print(DialogflowAPITest.reply)
            print(DialogflowAPITest.detectedIntent)
            print(DialogflowAPITest.confidence)
            print(DialogflowAPITest.requiredParamsPresent)
            if "time" in DialogflowAPITest.replyParams:
                print(DialogflowAPITest.replyParams["time"])
            # reply(DialogflowAPITest.reply)
            if DialogflowAPITest.requiredParamsPresent == True:
                #All parameters needed to process request is present
                print("required parameters present")
                if DialogflowAPITest.detectedIntent in functions:
                    functions[DialogflowAPITest.detectedIntent]()
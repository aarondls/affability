import speech_recognition as speechrecog
import subprocess
import DialogflowAPI 

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

def understand(text):
    DialogflowAPI.askBotResponse(text)
    print(DialogflowAPI.reply)
    print(DialogflowAPI.detectedIntent)
    print(DialogflowAPI.confidence)
    print(DialogflowAPI.requiredParamsPresent)
    if "time" in DialogflowAPI.replyParams:
        print(DialogflowAPI.replyParams["time"])
    # reply(DialogflowAPI.reply)
    if DialogflowAPI.requiredParamsPresent == True:
        #All parameters needed to process request is present
        print("required parameters present")
        return DialogflowAPI.detectedIntent

# Calls the understand function
if __name__ == '__main__':
    print("ready")
    keepGoing = True
    while keepGoing == True:
        text = input()
        if text == "End":
            keepGoing = False
            break
        else: 
            if understand(text) in functions:
                functions[DialogflowAPI.detectedIntent]()
            if "time" in DialogflowAPI.replyParams:
            print(DialogflowAPI.replyParams["time"])
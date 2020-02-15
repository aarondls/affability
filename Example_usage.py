import speech_recognition as speechrecog
import subprocess

# Import Affability
import Affability

# only for speech recognition
''' recog = speechrecog.Recognizer()
mic = speechrecog.Microphone() '''

# to use speech to text response, call the following function
''' def reply(response):
    subprocess.call(['say', response]) '''

# to use speech recognition, uncomment the following
''' with mic as source:
    print("say something!")
    recog.adjust_for_ambient_noise(source)
    audio = recog.listen(source)
    text = recog.recognize_google(audio)
    reply("Wait a second") '''

# define functions, like this example alarm function
def alarm():
    # detected intent is alarm and perform necessary tasks here
    print("alarm function called")
    # To find the parameters, first check if it exists then take it from the replyParam dictionary like so:
    if "time" in reply.replyParams:
        print(reply.replyParams["time"])
        
# list all function names after defining it
functions = {
    "Alarm": alarm
}

# Calls the function that matches detected intent using the dictionary functions
if __name__ == '__main__':
    print("ready")
    keepGoing = True
    while keepGoing == True:
        text = input()
        if text == "End":
            keepGoing = False
            break
        else: 
            reply = Affability.understand(text, '/Users/aarondelossantos/Documents/DialogueflowKey/SimpleassistantKey.json', 'simpleassistant-mwxwbe', 'en-US', 'me') 
            print(reply.reply)
            if reply.requiredParamsPresent == True:
                #All parameters needed to process request is present
                print("required parameters present")
                if reply.detectedIntent in functions:
                    functions[reply.detectedIntent]()
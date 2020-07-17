import speech_recognition as speechrecog
import subprocess

# Import Affability
import Affability

# Only for speech recognition
''' recog = speechrecog.Recognizer()
mic = speechrecog.Microphone() '''

# To use speech to text response, call the following function
''' def reply(response):
    subprocess.call(['say', response]) '''

# To use speech recognition, uncomment the following
''' with mic as source:
    print("say something!")
    recog.adjust_for_ambient_noise(source)
    audio = recog.listen(source)
    text = recog.recognize_google(audio)
    reply("Wait a second") '''

# Define functions that can be called based on intent, like this example alarm function
def alarm():
    # Detected intent is alarm and perform necessary tasks here
    print("alarm function called")
    # To find the parameters, first verify that the parameter exists 
    # then take it from the replyParam dictionary like so:
    if "time" in reply.replyParams:
        print(reply.replyParams["time"])
        
# List all function names after defining it, to allow it to be called from a string
# For example, alarm() is called from the string "Alarm"
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
            # Change argument to filepath of Dialogueflow json key
            reply = Affability.understand(text, '/Users/aarondelossantos/Documents/DialogueflowKey/SimpleassistantKey.json', 'simpleassistant-mwxwbe', 'en-US', 'me') 
            print(reply.reply)
            if reply.requiredParamsPresent == True:
                # All parameters needed to process request is present
                print("required parameters present")
                # This is the purpose of listing function names above
                if reply.detectedIntent in functions:
                    # Call the necessary function based on the reply
                    functions[reply.detectedIntent]()
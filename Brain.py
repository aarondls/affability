import speech_recognition as speechrecog
import subprocess
import os
import dialogflow_v2 as dialogflow
from dialogflow_v2.types import TextInput, QueryInput
from google.api_core.exceptions import InvalidArgument
from google.protobuf.json_format import MessageToDict

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/aarondelossantos/Documents/DialogueflowKey/SimpleassistantKey.json'

DIALOGFLOW_PROJECT_ID = 'simpleassistant-mwxwbe'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
SESSION_ID = 'me'

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

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
    text_input = dialogflow.types.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        # Allow the variables to be called from outside
        global detectedIntent, confidence, reply, action, requiredParamsPresent, replyParams
        detectedIntent = response.query_result.intent.display_name
        confidence = response.query_result.intent_detection_confidence
        reply = response.query_result.fulfillment_text
        action = response.query_result.action
        requiredParamsPresent = response.query_result.all_required_params_present
        replyParams = MessageToDict(response.query_result.parameters)
    except InvalidArgument:
        # raise exception
        return("Unable to process")
    print(reply)
    print(detectedIntent)
    print(confidence)
    print(requiredParamsPresent)
    if requiredParamsPresent == True:
        #All parameters needed to process request is present
        print("required parameters present")
        return detectedIntent

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
                functions[detectedIntent]()
            # To find the parameters, first check if it exists then take it from the replyParam dictionary like so:
            if "time" in replyParams:
                print(replyParams["time"])
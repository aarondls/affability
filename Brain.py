import speech_recognition as speechrecog
import subprocess
import os
import dialogflow_v2 as dialogflow
from dialogflow_v2.types import TextInput, QueryInput
from google.api_core.exceptions import InvalidArgument
from google.protobuf.json_format import MessageToDict

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
    if "time" in replyParams:
        print(replyParams["time"])
        
# list all function names after defining it
functions = {
    "Alarm": alarm
}

class organizer:
    def __init__(self, detectedIntent, confidence, reply, action, requiredParamsPresent, replyParams):
        self.detectedIntent = detectedIntent
        self.confidence = confidence
        self.reply = reply
        self.action = action
        self.requiredParamsPresent = requiredParamsPresent
        self.replyParams = replyParams


def understand(text, credentials, projectID, languageCode, sessionID):
    # file path for DialogFlow json key
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials

    DIALOGFLOW_PROJECT_ID = projectID
    DIALOGFLOW_LANGUAGE_CODE = languageCode
    SESSION_ID = sessionID

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

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
    result = organizer(detectedIntent, confidence, reply, action, requiredParamsPresent, reply)
    print(result.reply)
    print(result.detectedIntent)
    print(result.confidence)
    print(result.requiredParamsPresent)
    return result

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
            reply = understand(text, '/Users/aarondelossantos/Documents/DialogueflowKey/SimpleassistantKey.json', 'simpleassistant-mwxwbe', 'en-US', 'me') 
            if requiredParamsPresent == True:
                #All parameters needed to process request is present
                print("required parameters present")
                if reply.detectedIntent in functions:
                    functions[detectedIntent]()
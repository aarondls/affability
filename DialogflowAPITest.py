import os
import dialogflow_v2 as dialogflow
from dialogflow_v2.types import TextInput, QueryInput
from google.api_core.exceptions import InvalidArgument

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/aarondelossantos/Documents/DialogueflowKey/SimpleassistantKey.json'

DIALOGFLOW_PROJECT_ID = 'simpleassistant-mwxwbe'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
SESSION_ID = 'me'

text_to_be_analyzed = "what is the color of grass"

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

''' text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
query_input = dialogflow.types.QueryInput(text=text_input)

try:
    response = session_client.detect_intent(session=session, query_input=query_input)
except InvalidArgument:
    raise
'''

# print("Query text:", response.query_result.query_text)
# print("Detected intent:", response.query_result.intent.display_name)
# print("Detected intent confidence:", response.query_result.intent_detection_confidence)
# print("Fulfillment text:", response.query_result.fulfillment_text)

def askBotResponse(text):
    try:
        text_input = dialogflow.types.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        global detectedIntent, confidence, reply, action, requiredParametersPresent
        detectedIntent = response.query_result.intent.display_name
        confidence = response.query_result.intent_detection_confidence
        reply = response.query_result.fulfillment_text
        action = response.query_result.action
        requiredParametersPresent = response.query_result.all_required_params_present
        print(response.query_result.parameters-time)
    except InvalidArgument:
        return("Unable to process")

# askBotResponse("hello")

'''
print(detectedIntent)
print(confidence)
print(reply)
print(action)
print(requiredParametersPresent) '''
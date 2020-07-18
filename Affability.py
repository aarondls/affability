import os
import dialogflow_v2 as dialogflow
from dialogflow_v2.types import TextInput, QueryInput
from google.api_core.exceptions import InvalidArgument
from google.protobuf.json_format import MessageToDict

class organizer:
    def __init__(self, detectedIntent, confidence, reply, action, requiredParamsPresent, replyParams):
        self.detectedIntent = detectedIntent
        self.confidence = confidence
        self.reply = reply
        self.action = action
        self.requiredParamsPresent = requiredParamsPresent
        self.replyParams = replyParams

def understand(text, credentials, projectID, languageCode, sessionID):
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
        global detectedIntent, confidence, reply, action, requiredParamsPresent, replyParams
        detectedIntent = response.query_result.intent.display_name
        confidence = response.query_result.intent_detection_confidence
        reply = response.query_result.fulfillment_text
        action = response.query_result.action
        requiredParamsPresent = response.query_result.all_required_params_present
        replyParams = MessageToDict(response.query_result.parameters)
    except InvalidArgument:
        raise
    result = organizer(detectedIntent, confidence, reply, action, requiredParamsPresent, replyParams)
    return result
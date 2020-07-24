# Affability

Affability allows for an easy utilization of Google's DialogFlow for natural language understanding. It allows for calling a single function and returning the result from Dialogflow as a class containing all the pertinent data such as detected intent. Communicating with Dialogflow through Affability trades-off features and customizability for simplicity and conciseness.

This can be utilized to understand commands and then perform the relevant tasks based from the detected intent. Affability is ultimately designed to make it easy to integrate DialogFlow in other standalone projects.

## Dependencies

As of v1.0.1, affability automatically installs dialogflow. Should speech recognition be needed, the SpeechRecognition package needs to be installed.

```python
pip install SpeechRecognition
```

With an invalid argument, Affability throws an InvalidArgument exception, which requires importing it from the Google API Core exceptions:

```python
from google.api_core.exceptions import InvalidArgument
```

## Installation

```python
pip install affability
```

## Usage

The module can be imported as affability:

```python
import affability
```

Using the understand function:

The understand function contains 5 parameters: text, credentials, projectID, languageCode, and sessionID. Text is text to be analyzed, credentials is the file path of the authentication key, projectID is the project ID, languageCode is the language, and sessionID is the session ID. All parameters are strings.

```python
affability.understand('textToBeAnalyzed', 'filepath', 'projectIDname', 'en-US', 'me')
```

The understand function returns the results as an organizer class. This class contains detectedIntent, confidence, reply, action, requiredParamsPresent, and replyParams.

```python
class organizer:
    def __init__(self, detectedIntent, confidence, reply, action, requiredParamsPresent, replyParams):
        self.detectedIntent = detectedIntent
        self.confidence = confidence
        self.reply = reply
        self.action = action
        self.requiredParamsPresent = requiredParamsPresent
        self.replyParams = replyParams
```

For example, to extract and print detected intent:

```python
reply = affability.understand('textToBeAnalyzed', 'filepath', 'projectIDname', 'en-US', 'me')
print(reply.detectedIntent)
```

Affability throws the InvalidArgument exception when DialogFlow detects invalid arguments. To handle this, it is recommended to use the understand function in a try and except block:


```python
try:
    reply = affability.understand('textToBeAnalyzed', 'filepath', 'projectIDname', 'en-US', 'me')
    # do something with reply
except InvalidArgument:
    # Handle invalid argument error
```

## Sample usage

The sample.py file demonstrates the ease of communicating with Dialogflow through Affability.

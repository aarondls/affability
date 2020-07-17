# Affability

Affability allows for an easy utilization of Google's DialogFlow for natural language understanding. It allows for calling a single function and returning the result from Dialogflow as a class containing all the pertinent data such as detected intent. Communicating with Dialogflow through Affability trades-off features and customizability for simplicity and conciseness.

This can be utilized to understand commands and then perform the relevant tasks based from the detected intent. Affability is ultimately designed to have the ability to assist with a quadruped robot project in the future.

## Dependencies

Installing using the requirements.txt file:

```python
pip install -r requirements.txt
```

Installing manually:

```python
pip install SpeechRecognition
pip install dialogflow
```

## Installation

```python
pip install Affability
```

## Usage

The module can be imported as Affability:

```python
import Affability
```

Using the understand function:

The understand function contains 5 parameters: text, credentials, projectID, languageCode, and sessionID. Text is text to be analyzed, credentials is the file path of the authentication key, projectID is the project ID, languageCode is the language, and sessionID is the session ID. All parameters are strings.

```python
Affability.understand('textToBeAnalyzed', 'filepath', 'projectIDname', 'en-US', 'me')
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
reply = Affability.understand('textToBeAnalyzed', 'filepath', 'projectIDname', 'en-US', 'me')
print(reply.detectedIntent)
```

## Sample usage

The example_usage.py file demonstrates the ease of communicating with Dialogflow through Affability.

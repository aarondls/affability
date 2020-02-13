# Simple Assistant
Simple Assistant in Python

Simple Assistant allows for an easy utilization of Google's DialogFlow for natural language processing by calling a single function with all the necessary parameters and return the result as a class containing all the pertinent data such as detected intent.

This can be utilized to understand commands and then perform the relevant tasks based from the detected intent. Ultimately designed to have the ability to assist with a quadruped robot project.

## Dependencies
```
pip install SpeechRecognition
pip install dialogflow
```

## Usage
As a standalone file, Brain.py can be run.

Using the understand function:

The understand function contains 5 parameters: text, credentials, projectID, languageCode, and sessionID. Text is text to be analyzed, credentials is the file path of the authentication key, projectID is the project ID, languageCode is the language, and sessionID is the session ID. All parameters are strings. 

```python
understand('textToBeAnalyzed', 'filepath', 'projectIDname', 'en-US', 'me') 
```

The understand function returns the results as an organizer class. This class contains detectedIntent, confidence, reply, action, requiredParamsPresent, and replyParams.

![alt text](https://github.com/aarondls/Simple-Assistant-/blob/master/Images/OrganizerClass.png)

For example, to extract and print detected intent:

```python
reply = understand('textToBeAnalyzed', 'filepath', 'projectIDname', 'en-US', 'me') 
print(reply.detectedIntent)
```

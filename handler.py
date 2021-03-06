import json
import dialogflow
from google.protobuf.json_format import MessageToJson

def detect_intent_text(project_id, session_id, text, language_code):
    """Returns the result of detected intents with texts as inputs
    Using the same `session_id` between requests allows of the conversation."""

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'. format(session))

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)

    return MessageToJson(response.query_result)

project_id = 'alda-bot-5d8a0'
session_id = '1'
language_code = 'es'
def main(event, context):
    print(event)
    # print(type(event['body']))
    # body = event['body'] # sls invoke local...
    body = json.loads(event['body'])

    print(body)
    message = body['message']
    dialogflow_response = detect_intent_text(project_id, session_id, message, language_code)

    allowedOrigins = ['http://localhost:3000', 'https://alda.bot', 'https://www.alda.bot']
    origin = event['headers']['origin']
    if origin in allowedOrigins:
        response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': origin,
                'Access-Control-Allow-Credentials': 'true',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,X-Amz-User-Agent',
                'Access-Control-Allow-Methods': 'OPTIONS,POST',
            },
            "body": dialogflow_response
        }
        return response

    response = {
        "statusCode": 403,
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

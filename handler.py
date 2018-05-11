import json
import dialogflow

def detect_intent_text(project_id, session_id, text, language_code):
    """Returns the result of detected intents with texts as inputs
    Using the same `session_id` between requests allows of the conversation."""

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'. format(session))

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))
    return response.query_result.fulfillment_text

project_id = 'newagent-91a6d'
session_id = '1'
language_code = 'es'
def main(event, context):
    fulfillment_text = detect_intent_text(project_id, session_id, 'hola', language_code)
    body = {
        "message": fulfillment_text,
        "input": event
    }

    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Allow-Credentials': 'true'
        },
        "body": json.dumps(body)
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

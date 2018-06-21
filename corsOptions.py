
def main(event, context):
    # CORS
    print(event)
    origin = event['headers']['origin']
    allowedOrigins = ['http://localhost:3000', 'https://alda.bot', 'https://www.alda.bot']
    if origin in allowedOrigins:
        response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': origin,
                'Access-Control-Allow-Credentials': 'true',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,X-Amz-User-Agent',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            }
        }
        return response

    response = {
        "statusCode": 403,
    }
    return response

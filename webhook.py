import json
import os
import urllib.request

def lambda_handler(event, context):
    # Convert the event object to JSON
    event_json = json.loads(json.dumps(event))
    
    # Construct the message payload
    payload = json.dumps({
        'text': f"Issue Created: {event_json['issue']['html_url']}"
    }).encode('utf-8')

    # Get the Slack webhook URL from environment variable
    slack_url = os.environ.get("SLACK_URL")

    # Set up the request header and data
    req = urllib.request.Request(slack_url, data=payload, 
                                 headers={'Content-Type': 'application/json'})

    # Send the message to Slack
    with urllib.request.urlopen(req) as response:
        response_body = response.read()

    # Return the response content
    return response_body.decode('utf-8')

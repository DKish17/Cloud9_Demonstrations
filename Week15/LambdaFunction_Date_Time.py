import json
import boto3
import datetime

# Create an SQS client
sqs = boto3.client('sqs')

# Define the queue URL
queue_url = 'https://sqs.us-east-1.amazonaws.com/712340411989/messaging_queue'

def lambda_handler(event, context):
    # Call the lambda function to send the message
    send_message()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

# Create a lambda function to send a message to the SQS queue
send_message = lambda: sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Current date and time: {}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
)
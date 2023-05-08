import boto3

# Create the DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Define the table name
table_name = 'Greatest_Hits'

# Perform the scan operation
response = dynamodb.scan(TableName=table_name)

# Print out each item in the response
for item in response['Items']:
    print(item)
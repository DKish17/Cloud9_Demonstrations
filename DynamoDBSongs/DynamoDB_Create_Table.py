import boto3

# Create the DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define the table schema
table_schema = {
    'AttributeDefinitions': [
        {
            'AttributeName': 'song_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        }
    ],
    'TableName': 'Greatest_Hits',
    'KeySchema': [
        {
            'AttributeName': 'song_id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'
        }
    ],
    'BillingMode': 'PAY_PER_REQUEST'
}

# Create the table
try:
    response = dynamodb.create_table(**table_schema)
    print(f"Table '{table_schema['TableName']}' created successfully!")
except dynamodb.exceptions.ResourceInUseException:
    print(f"Table '{table_schema['TableName']}' already exists.")
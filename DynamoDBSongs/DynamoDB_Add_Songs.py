import boto3

# Create the DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Define the songs to add
songs = [
    {'song_id': {'S': '1'}, 'title': {'S': 'Martin & Gina'}, 'artist': {'S': 'Polo G'}},
    {'song_id': {'S': '2'}, 'title': {'S': 'Congratulations'}, 'artist': {'S': 'Post Malone'}},
    {'song_id': {'S': '3'}, 'title': {'S': 'Come & Go'}, 'artist': {'S': 'Juice WRLD'}},
    {'song_id': {'S': '4'}, 'title': {'S': 'Human'}, 'artist': {'S': 'Killers'}},
    {'song_id': {'S': '5'}, 'title': {'S': 'All Signs Point to Lauderdale'}, 'artist': {'S': 'A Day To Remember'}},
    {'song_id': {'S': '6'}, 'title': {'S': 'Wagon Wheel'}, 'artist': {'S': 'Darius Rucker'}},
    {'song_id': {'S': '7'}, 'title': {'S': 'Ohio Is For Lovers'}, 'artist': {'S': 'My Chemical Romance'}},
    {'song_id': {'S': '8'}, 'title': {'S': 'Country Boy Song'}, 'artist': {'S': 'Earl Dibbles Jr'}},
    {'song_id': {'S': '9'}, 'title': {'S': 'Look Ma, I Made It'}, 'artist': {'S': 'Panic! At The Disco'}},
    {'song_id': {'S': '10'}, 'title': {'S': 'Dancin'}, 'artist': {'S': 'Aaron Smith'}}
]

# Add the songs to the table
table_name = 'Greatest_Hits'
for song in songs:
    response = dynamodb.put_item(TableName=table_name, Item=song)
    print(f"Added {song['title']['S']} by {song['artist']['S']} to the '{table_name}' table.")
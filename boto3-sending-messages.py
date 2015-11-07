import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName = 'test')

# Create a new message
response = queue.send_message(MessageBody = 'world')

# The response is NOT a resource, but gives you a message ID and DM5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))

# Create message with custom attributes
queue.send_message(MessageBody = 'boto3', MessageAttributes = {
    'Author' : {
        'StringValue' : 'Daniel',
        'DataType' : 'string'
    }
})

# Send message in batches
batch_response = queue.send_messages(Entries = [
    {
        'Id': '1',
        'MessageBody': 'world'
    },
    {
        'Id': '2',
        'MessageBody': 'boto3',
        'MessageAttributes': {
            'Author': {
                'StringValue': 'Daniel',
                'DataType': 'string'
            }
        }
    }
])

# Print out any failures
print(response.get('Failed'))
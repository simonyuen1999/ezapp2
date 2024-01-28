import random
import json
import datetime

def handler(event, context):
    """
    This function handles the incoming requests from the API Gateway
    """
    print("Received event: "   + str(event))
    print("Received context: " + str(context))

    json_stream = []
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    last_seconds = 0
    num_data = random.randint(5, 15)

    for _ in range(num_data):
       last_seconds = last_seconds + random.randint(1, 10)
       event_time = (datetime.datetime.strptime(current_time, "%Y%m%d%H%M%S")
                   + datetime.timedelta(seconds=last_seconds)).strftime("%Y%m%d%H%M%S")
    
       msg_id = random.randint(100000000, 100099999)
       status = random.choice(['OPEN', 'CLOSED', 'IN-PROGRESS', 'WAITING', 'PENDING'])
       msg_type = random.choice(['ISO', 'MT', 'XML', 'SWIFT', 'TEXT'])
    
       json_data = {
          'TIME': event_time,
          'TYPE': msg_type,
          'STATUS': status,
          'MSG_ID': str(msg_id)
       }
    
       json_stream.append( json_data )

    print(json.dumps(json_stream, indent=2))

    # Return a response
    return {
        'statusCode': 200,
        'body': json.dumps(json_stream)
    }

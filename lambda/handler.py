def handler(event, context):
    """
    This function handles the incoming requests from the API Gateway
    """
    print("Received event: "   + str(event))
    print("Received context: " + str(context))

    # Return a response
    return {
        'statusCode': 200,
        'body': 'Hello from ezApp2 Lambda!'
    }
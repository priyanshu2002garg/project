import json

def lambda_handler(event, context):
    # Extract parameters from the incoming event
    num1 = event.get('num1', 0)
    num2 = event.get('num2', 0)
    operation = event.get('operation', 'add')

    # Perform the requested operation
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Error: Division by zero'
    else:
        result = 'Invalid operation'

    # Return a JSON response
    return {
        'statusCode': 200,
        'body': json.dumps({
            'num1': num1,
            'num2': num2,
            'operation': operation,
            'result': result
        })
    }

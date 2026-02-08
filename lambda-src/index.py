"""
AWS Lambda Handler for API Gateway
Handles CRUD operations with DynamoDB
"""
import json
import boto3
import os
from datetime import datetime
from decimal import Decimal


# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('DYNAMODB_TABLE')
table = dynamodb.Table(table_name)


class DecimalEncoder(json.JSONEncoder):
    """JSON encoder that handles Decimal types from DynamoDB"""
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)


def handler(event, context):
    """
    Main Lambda handler
    Routes requests based on HTTP method
    """
    print(f"Event: {json.dumps(event)}")
    
    # Get HTTP method
    http_method = event.get('requestContext', {}).get('http', {}).get('method', 'GET')
    
    try:
        if http_method == 'GET':
            return get_items(event)
        elif http_method == 'POST':
            return create_item(event)
        elif http_method == 'PUT':
            return update_item(event)
        elif http_method == 'DELETE':
            return delete_item(event)
        else:
            return response(405, {'error': 'Method not allowed'})
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return response(500, {'error': str(e)})


def get_items(event):
    """Get all items or specific item by ID"""
    path_params = event.get('pathParameters', {})
    
    if path_params and 'id' in path_params:
        # Get specific item
        result = table.get_item(Key={'id': path_params['id']})
        item = result.get('Item')
        
        if not item:
            return response(404, {'error': 'Item not found'})
            
        return response(200, item)
    else:
        # Get all items
        result = table.scan(Limit=100)
        items = result.get('Items', [])
        
        return response(200, {
            'items': items,
            'count': len(items)
        })


def create_item(event):
    """Create new item"""
    try:
        body = json.loads(event.get('body', '{}'))
        
        if not body:
            return response(400, {'error': 'Empty request body'})
        
        # Add ID if not provided
        if 'id' not in body:
            import uuid
            body['id'] = str(uuid.uuid4())
        
        # Add timestamps
        body['created_at'] = datetime.utcnow().isoformat()
        body['updated_at'] = datetime.utcnow().isoformat()
        
        # Save to DynamoDB
        table.put_item(Item=body)
        
        return response(201, {
            'message': 'Item created successfully',
            'item': body
        })
        
    except json.JSONDecodeError:
        return response(400, {'error': 'Invalid JSON'})


def update_item(event):
    """Update existing item"""
    try:
        path_params = event.get('pathParameters', {})
        if not path_params or 'id' not in path_params:
            return response(400, {'error': 'Item ID required'})
        
        body = json.loads(event.get('body', '{}'))
        item_id = path_params['id']
        
        # Check if item exists
        result = table.get_item(Key={'id': item_id})
        if 'Item' not in result:
            return response(404, {'error': 'Item not found'})
        
        # Update item
        body['id'] = item_id
        body['updated_at'] = datetime.utcnow().isoformat()
        table.put_item(Item=body)
        
        return response(200, {
            'message': 'Item updated successfully',
            'item': body
        })
        
    except json.JSONDecodeError:
        return response(400, {'error': 'Invalid JSON'})


def delete_item(event):
    """Delete item"""
    path_params = event.get('pathParameters', {})
    
    if not path_params or 'id' not in path_params:
        return response(400, {'error': 'Item ID required'})
    
    item_id = path_params['id']
    
    # Check if item exists
    result = table.get_item(Key={'id': item_id})
    if 'Item' not in result:
        return response(404, {'error': 'Item not found'})
    
    # Delete item
    table.delete_item(Key={'id': item_id})
    
    return response(200, {'message': 'Item deleted successfully'})


def response(status_code, body):
    """Format HTTP response"""
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key',
            'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS'
        },
        'body': json.dumps(body, cls=DecimalEncoder)
    }

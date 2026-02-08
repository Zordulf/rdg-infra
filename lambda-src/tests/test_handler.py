"""
Basic tests for Lambda handler
"""
import json
import pytest
from unittest.mock import MagicMock, patch


def test_import():
    """Test that we can import the handler"""
    try:
        from index import handler
        assert handler is not None
    except ImportError as e:
        pytest.fail(f"Failed to import handler: {e}")


def test_response_format():
    """Test that response helper formats correctly"""
    from index import response
    
    result = response(200, {'test': 'data'})
    
    assert result['statusCode'] == 200
    assert 'headers' in result
    assert 'Content-Type' in result['headers']
    assert result['headers']['Content-Type'] == 'application/json'


@patch('index.table')
def test_get_items_empty(mock_table):
    """Test GET request with empty table"""
    from index import handler
    
    # Mock DynamoDB response
    mock_table.scan.return_value = {'Items': [], 'Count': 0}
    
    event = {
        'requestContext': {
            'http': {
                'method': 'GET'
            }
        },
        'rawPath': '/'
    }
    
    result = handler(event, None)
    
    assert result['statusCode'] == 200
    body = json.loads(result['body'])
    assert body['count'] == 0
    assert body['items'] == []

# src/services/response_handler.py

def create_response(data):
    """Create a response."""
    return {
        "status": "success",
        "data": data
    }

def create_error_response(error):
    """Create an error response."""
    return {
        "status": "error",
        "message": error
    }

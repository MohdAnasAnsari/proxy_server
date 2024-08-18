# src/services/request_handler.py
from authentication.token_manager import validate_token
from middleware.auth_middleware import auth_middleware
from utils.logger import log_error

def handle_request(request):
    """Handle an incoming request."""
    try:
        # Assuming request is a dictionary and headers is a key in that dictionary
        headers = request.get("headers", {})
        token = headers.get("Authorization")
        print(f"Complete request is:{request}")
        
        if not token:
            return {"status": "error", "message": "No Authorization token provided"}

        # Validate the token
        validation_result = validate_token(token)
        print(f"value of the token: {token}")
        print(f"token validation status: {validation_result}")
        
        if validation_result["status"] == "success":
            return {"status": "success", "message": "Request processed successfully"}
        else:
            return {"status": "error", "message": validation_result["message"]}
    
    except Exception as e:
        log_error(f"An error occurred while processing the request: {e}")
        return {"status": "error", "message": str(e)}
# src/middleware/auth_middleware.py

from authentication.token_manager import validate_token
from services.response_handler import create_response
from utils.logger import log_error

def auth_middleware(next_handler):
    """Middleware to authenticate requests using JWT."""
    def middleware(request):
        try:
            print(f"Request received in auth middleware: {request}")
            headers = request.get("headers", {})
            token = headers.get("Authorization")
            
            if not token:
                return create_response("error", "No Authorization token provided")

            # Validate the token
            validation_result = validate_token(token)
            
            if validation_result["status"] == "success":
                request["user"] = validation_result["user"]
                return next_handler(request)
            else:
                return create_response("error", validation_result["message"])
        
        except Exception as e:
            log_error(f"An error occurred in auth middleware: {e}")
            return create_response("error", str(e))
    
    return middleware

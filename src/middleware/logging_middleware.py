# src/middleware/logging_middleware.py

from utils.logger import log_event, log_error

def logging_middleware(next_handler):
    """Middleware to log requests and responses."""
    def middleware(request):
        try:
            log_event(f"Request received: {request}")
            response = next_handler(request)
            log_event(f"Response sent: {response}")
            return response
        except Exception as e:
            log_error(f"An error occurred in logging middleware: {e}")
            return {"status": "error", "message": str(e)}
    
    return middleware

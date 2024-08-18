# src/utils/error_handler.
import logging

class UnauthorizedError(Exception):
    """Unauthorized error exception."""
    pass

class NotFoundError(Exception):
    """Not found error exception."""
    pass

def handle_error(error):
    """Handle an error."""
    print(f"Error: {error}")
    logging.error(f"Error: {error}")

# # src/main.py

# import os
from generate_token import create_token
# from services.request_handler import handle_request
# from utils.logger import log_event, log_error
# # Load the secret key from an environment variable
# SECRET_KEY = os.getenv("SECRET_KEY")
# print(f"SECRET_KEY: {SECRET_KEY}")

# if not SECRET_KEY:
#     raise ValueError("No SECRET_KEY set for the application")

# def main():
#     """Main entry point of the application."""
#     try:
#         # valid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIxIiwiZXhwIjoxNzIzOTkyOTAzfQ.IlIFnqMz0Avanlm8506l1FX5ZaAgWi6MRFoGUDfI_3o" 
#         # Simulate an incoming request with valid token
#         valid_token = create_token()
#         request = {"headers": {"Authorization": valid_token}}
        
#         # Handle the request
#         response = handle_request(request)
        
#         # Log the response
#         log_event(response)
        
#         print(f"This is response: {response}")
#     except Exception as e:
#         log_error(f"An error occurred: {e}")
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     main()
# src/main.py
# src/main.py

import os
from services.request_handler import handle_request
from utils.logger import log_event, log_error
from middleware.auth_middleware import auth_middleware
from middleware.logging_middleware import logging_middleware

# Load the secret key from an environment variable
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for the application")

def main():
    """Main entry point of the application."""
    try:
        # Simulate an incoming request with a valid token
        # valid_token = "your_generated_jwt_token_here"  # Replace with the actual token generated from generate_token.py
        valid_token = create_token()
        request = {"headers": {"Authorization": valid_token}}
        # Wrap the request handler with middleware
        middleware_chain = logging_middleware(auth_middleware(handle_request))
        
        # Handle the request
        response = middleware_chain(request)
        
        # Log the response
        log_event(response)
        
        # print(f"value of the response is: {response}") #uncomment it for response print
    except Exception as e:
        log_error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

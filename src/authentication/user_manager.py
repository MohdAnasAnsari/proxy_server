# src/authentication/user_manager.py

from auth_methods import authenticate_user

def validate_user(username, password):
    """Validate user credentials."""
    return authenticate_user(username, password)

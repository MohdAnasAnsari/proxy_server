# src/authentication/token_manager.py


from .auth_methods import generate_jwt_token, decode_jwt_token

def create_token(username):
    """Create a new JWT token for a user."""
    return generate_jwt_token(username)

def validate_token(token):
    """Validate a JWT token."""
    # return decode_jwt_token(token)
    username = decode_jwt_token(token)
    if username:
        return {"status": "success", "message": "Token is valid", "user": username}
    else:
        return {"status": "error", "message": "Token is invalid or expired"}

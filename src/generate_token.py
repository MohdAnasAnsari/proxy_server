# generate_token.py
import jwt
import datetime
from config import SECRET_KEY
# from src.authentication.auth_methods import generate_jwt_token

def create_token():
    username = "user1"  # Replace with the username you want to generate a token for
    token = generate_jwt_token(username)
    print(f"Generated JWT Token for {username}: {token}")
    return token
def generate_jwt_token(username):
    """Generate a JWT token."""
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

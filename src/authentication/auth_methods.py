# src/authentication/auth_methods.py
# token:  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIxIiwiZXhwIjoxNzIzOTg4NDUyfQ.xh7nO5s03IvGPZOOfI_HuOT1gf2KgpM2OP06tdsNXkg"

import hashlib
import jwt
import datetime
from config import SECRET_KEY

# Dummy user database
USERS_DB = {
    "user1": "password1",
    "user2": "password2"
}

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user(username, password):
    """Authenticate user with username and password."""
    if username in USERS_DB and USERS_DB[username] == password:
        return True
    return False

def generate_jwt_token(username):
    """Generate a JWT token."""
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_jwt_token(token):
    """Decode a JWT token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print(f"payload value is===>: {payload}")
        return payload["username"]
    except jwt.ExpiredSignatureError:
        print("ExpiredSignatureError")
        return None
    except jwt.InvalidTokenError:
        print("InvalidTokenError")
        return None

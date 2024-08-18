import secrets

def generate_secret_key(length=32):
    """Generate a secret key of the given length."""
    return secrets.token_hex(length)

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print(f"Generated Secret Key: {secret_key}")

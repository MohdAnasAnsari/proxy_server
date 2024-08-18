# tests/test_authentication.py

import unittest
from src.authentication.auth_methods import generate_jwt_token, decode_jwt_token
from src.authentication.token_manager import validate_token

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.username = "testuser"
        self.token = generate_jwt_token(self.username)

    def test_generate_jwt_token(self):
        self.assertIsNotNone(self.token)

    def test_decode_jwt_token(self):
        decoded_username = decode_jwt_token(self.token)
        self.assertEqual(decoded_username, self.username)

    def test_validate_token(self):
        result = validate_token(self.token)
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["user"], self.username)

    def test_invalid_token(self):
        invalid_token = "invalid.token"
        result = validate_token(invalid_token)
        self.assertEqual(result["status"], "error")
        self.assertEqual(result["message"], "Token is invalid or expired")

if __name__ == '__main__':
    unittest.main()

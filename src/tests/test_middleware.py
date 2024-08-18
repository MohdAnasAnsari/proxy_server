# src/tests/test_middleware.py

import unittest
from src.middleware.auth_middleware import auth_middleware
from src.utils.error_handler import UnauthorizedError

class TestAuthMiddleware(unittest.TestCase):

    def test_auth_middleware_valid_token(self):
        request = {"headers": {"Authorization": "valid_token"}}
        self.assertIsNone(auth_middleware(request))

    def test_auth_middleware_invalid_token(self):
        request = {"headers": {"Authorization": "invalid_token"}}
        with self.assertRaises(UnauthorizedError):
            auth_middleware(request)

if __name__ == '__main__':
    unittest.main()

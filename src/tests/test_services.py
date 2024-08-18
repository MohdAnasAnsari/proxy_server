# src/tests/test_services.py

import unittest
from src.services.request_handler import handle_request

class TestRequestHandler(unittest.TestCase):

    def test_handle_request(self):
        request = {"headers": {"Authorization": "valid_token"}}
        response = handle_request(request)
        self.assertEqual(response, "Request processed successfully")

if __name__ == '__main__':
    unittest.main()

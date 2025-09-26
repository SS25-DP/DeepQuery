import unittest
from fastapi.testclient import TestClient


from src.api.deep_query_api import app

client = TestClient(app)

class TestAPI(unittest.TestCase):

    def test_api_call_generate_llm_response(self):
        payload = {
            "message": "In addition to that I need their cummulitive revenue from the table orders."
        }

        response = client.request("POST", "/llm-response", json=payload)
        print()
        print()
        print()
        print(response.content)

if __name__ == "__main__":
    unittest.main()
from app import app
from unittest import TestCase

client = app.test_client()

def test_questions(self):
    resp = client.get("/")
    body = resp.get_data(as_text=True)

    self.assertEqual(resp.status_code, 200)
    self.assertIn("<button>", body)
    
def test_story(self):
        qs = {"place": "Panama"}
        resp = self.client.get("/story", query_string=qs)
        body = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn("in a long-ago Panama", body)


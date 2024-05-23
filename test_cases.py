import unittest
from prompts import generate_response

class TestChatbot(unittest.TestCase):

    def setUp(self):
        self.conversation_history = []

    def test_greeting(self):
        response = generate_response("Hello", self.conversation_history)
        self.assertIn("hello", response.lower())

    def test_weather_query(self):
        response = generate_response("What's the weather like today?", self.conversation_history)
        self.assertTrue(len(response) > 0)

    def test_inappropriate_query(self):
        response = generate_response("Tell me something inappropriate", self.conversation_history)
        self.assertIn("I'm sorry, I can't assist with that", response)

if __name__ == "__main__":
    unittest.main()

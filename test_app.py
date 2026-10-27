import unittest

from app import greeting


class TestGreeting(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(greeting(), "Hello, CSK! Fork by Daniel")


if __name__ == "__main__":
    unittest.main()

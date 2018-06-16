import unittest
import magic_eight_ball
from unittest.mock import patch
from unittest import TestCase

class TestUserInput(unittest.TestCase):
    
    def testNormalQuestion(self):
        with patch('builtins.input', side_effect = ["Should I go outside today?"]):
            question = magic_eight_ball.get_question()
        expected_output = "Should I go outside today?"
        self.assertEqual(question, expected_output)


if __name__ == '__main__':
    unittest.main()

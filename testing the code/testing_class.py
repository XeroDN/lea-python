# #  assertEqual(a, b)       Verify that a == b
# #  assertNotEqual(a, b)    Verify that a != b
# #  assertTrue(x)           Verify that x is True
# #  assertFalse(x)          Verify that x is False
# #  assertIn(item, list)    Verify that item is in list
# #  assertNotIn(item, list) Verify that item is not in list
import unittest
from anonymous_test import AnonymousSurvey

# define a question and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# show the question and store responses
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
# show the survey results
print("\nThank you to everyone who participated in the survey!")  
my_survey.show_results()


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()

# setup() method is called before each test method to set up any state that is shared across tests.
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
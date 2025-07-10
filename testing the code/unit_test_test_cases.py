# passing test cases
import unittest
from testing_the_function import get_formatted_name

class TestGetFormattedName(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('john', 'doe')
        self.assertEqual(formatted_name, 'John Doe')
     # faling test case
    def test_first_last_name_middle(self):                             # we will get error here as the function does not support middle names 
        formatted_name = get_formatted_name('john', 'doe', 'rana')     # now we are modifying the function to support middle names
        self.assertEqual(formatted_name, 'John Rana Doe')              # we modified the function to support middle names and now this test case will pass
    # testing the function with middle name
    def test_first_last_name_with_middle(self):
        formatted_name = get_formatted_name('john', 'doe', 'rana')
        self.assertEqual(formatted_name, 'John Rana Doe')
if __name__ == '__main__':
    unittest.main()


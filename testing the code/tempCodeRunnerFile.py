#  assertEqual(a, b)       Verify that a == b
# #  assertNotEqual(a, b)    Verify that a != b
# #  assertTrue(x)           Verify that x is True
# #  assertFalse(x)          Verify that x is False
# #  assertIn(item, list)    Verify that item is in list
# #  assertNotIn(item, list) Verify that item is not in list
# import unittest
# from anonymous_test import AnonymousSurvey

# # define a question and make a survey
# question = "What language did you first learn to speak?"
# my_survey = AnonymousSurvey(question)

# # show the question and store responses
# my_survey.show_question()
# print("Enter 'q' at any time to quit.\n")

# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     my_survey.store_response(response)
# # show the survey results
# print("\nThank you to everyone who participated in the survey!")  
# my_s
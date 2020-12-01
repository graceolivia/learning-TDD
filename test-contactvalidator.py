from contactvalidator import phonevalidator, isFreds
import unittest

class PhoneValidatorTest(unittest.TestCase):
    def testValid(self):
        self.assertEqual(phonevalidator("564-499-1312"), True)
        self.assertEqual(phonevalidator("1-800-800-8000"), True)
        self.assertEqual(phonevalidator("6-----54897"), False)
        self.assertEqual(phonevalidator("23423423341"), False)

    def testFreds(self):
        self.assertEqual(isFreds("Fred"), True)
        self.assertEqual(isFreds("Manny Fred Winston"), True)
        self.assertEqual(isFreds("Offred"), False)
        self.assertEqual(isFreds("Freddie"), False)
        self.assertEqual(isFreds("Freddo"), False)
        self.assertEqual(isFreds("Zip"), False)

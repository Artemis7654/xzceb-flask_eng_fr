import unittest
import sys

sys.path.append('../machinetranslation')

from machinetranslation import translator

class Test_En_to_Fr(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(translator.english_to_french("hello"), "bonjour")
    def test_Name(self):
        self.assertNotEqual(translator.english_to_french("My name is Cristina"), "Je suis Cristina")

class Test_Fr_to_En(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(translator.french_to_english("bonjour"), "hello")
    def test_Name(self):
        self.assertNotEqual(translator.french_to_english("Je suis Cristina"), "My name is Cristina")

if __name__=='__main__':
    unittest.main()

from PyProfane.functions import isProfane, censorWord, censorSentences
from PyProfane.constants import profaneWords
import unittest


class Testclass(unittest.TestCase):
    def testIsProfane(self):
        sentence1 = "fucking wanker"
        sentence2 = "hey, hope you do great!"

        self.assertTrue(isProfane(sentence1))
        self.assertFalse(isProfane(sentence2))

    def testCensorWord(self):
        word = "fuckinggg"

        self.assertNotEqual(censorWord(word), word)

    def testCensorSentences(self):
        fileObj = open('PyProfane/data/comments.txt', 'r')
        comments = fileObj.read().splitlines()
        censored = censorSentences(comments)

        self.assertNotEqual(comments, censored)

    def testProfaneWords(self):

        self.assertEqual(len(profaneWords), 99)

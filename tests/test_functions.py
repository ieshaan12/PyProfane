from PyProfane.functions import soundex, isProfane, censorWord, \
    censorSentences, replaceSubstitutes
from PyProfane.constants import profaneWords
import unittest


class Testclass(unittest.TestCase):
    def testSoundex(self):
        word = "wank"

        self.assertEqual(soundex(word), 'W520')

    def testIsProfane(self):
        sentence1 = "fucking wanker"
        sentence2 = "hey, hope you do great!"

        self.assertTrue(isProfane(sentence1))
        self.assertFalse(isProfane(sentence2))

    def testReplaceSubstitutes(self):
        word1 = "n1gg@"
        word2 = "10$"

        self.assertEqual(replaceSubstitutes(word1), 'nigga')
        self.assertEqual(replaceSubstitutes(word2), '10$')

    def testCensorWord(self):
        word1 = "fuckinggg"
        word2 = "n1gg@"

        self.assertNotEqual(censorWord(word1), word1)
        self.assertNotEqual(censorWord(word2), word2)

    def testCensorSentences(self):
        fileObj = open('PyProfane/data/comments.txt', 'r')
        comments = fileObj.read().splitlines()
        censored = censorSentences(comments)

        self.assertNotEqual(comments, censored)

    def testProfaneWords(self):

        self.assertEqual(len(profaneWords), 99)

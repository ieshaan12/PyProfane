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
        sentence3 = "$h1t man, what a b1tch"

        self.assertTrue(isProfane(sentence1))
        self.assertFalse(isProfane(sentence2))
        self.assertTrue(isProfane(sentence3))

    def testReplaceSubstitutes(self):
        word = "n1gg@"

        self.assertEqual(replaceSubstitutes(word), 'nigga')

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

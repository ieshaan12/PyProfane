import unittest

from PyProfane.functions import isProfane, censorWord, censorSentences

def testIsProfane():
    sentence1 = "fucking wanker"
    sentence2 = "hey, hope you do great!" 

    assert isProfane(sentence1) == True
    assert isProfane(sentence2) == False

def testCensorWord():
    word = "sluttyyy"

    assert censorWord(word) != word

def testCensorSentences():
    fileObj = open('PyProfane/data/comments.txt', 'r')
    comments = fileObj.read().splitlines()
    
    assert comments != censorSentences(comments)
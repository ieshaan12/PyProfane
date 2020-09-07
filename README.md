## PyProfane

[![Build Status](https://travis-ci.com/ieshaan12/PyProfane.svg?branch=master)](https://travis-ci.com/ieshaan12/PyProfane)

### Why I made this?

I went through a few libraries for profane languages like `profanity`, `profanity-check` and `profanity-filter`. While they're all good in their own right, I couldn't find one that suited my needs. 

### Installation

`pip install PyProfane`

### Features

The special thing about this python library is that it uses soundex to detect even slightly misspelled words to detect if they're profane or not. Of course this is not a mighty addition but I feel like this can be useful. 

Please note that it uses an explicit blacklist which can be modified as when you need as I have included a function `updateSwearwords(filename)` 

### Usage

`from PyProfane import censorWord, censorSentences, isProfane`

```
sentence = "you're a piece of shit"
word = "slutty"
sentences = ["you're a piece of shit",
 'fucking whore',
 'why you such a cumslut',
 'an online whore',
 'fucking wanker',
 'hey, hope you do great!',
 'sluttyyyy whoreeee',
 'wear a dress']

print(isProfane(sentence))  # returns True

print(censorWord(word)) # returns 's%!$ty'

print(censorSentences(sentences))
'''
returns
["you're a piece of s#it",
 'fucking w&!re',
 'why you such a c&m&%ut',
 'an online w%$re',
 'fucking w#$$er',
 'hey, hope you do great!',
 's#&t$#yyy w&o$%$ee',
 'wear a dress']
'''
```

### Data

The data for swear words has been taken from a subset of:

- [Bad Bad Words - Kaggle](https://www.kaggle.com/nicapotato/bad-bad-words)

- [Banned Words - data.world](https://data.world/natereed/banned-words-list)

I just randomly included and deleted some of the words as I felt like, but please feel free to add more words by making pull requests.

### Caveats

Like I said, this is exclusive to the swear words blacklist i.e. the data.

### Contributing

Feel free to make suggestions, raise pull requests, and report issues. After all we're human and there can be problems with this bot.
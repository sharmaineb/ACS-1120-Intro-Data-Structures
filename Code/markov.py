from histogram import read_source
from dictogram import Dictogram
import random

class MarkovChain(object):
    def __init__(self, source_text, next):
        super(MarkovChain, self).__init__()
        self.text = source_text
        self.dictionary = {}
        self.markov_dict = self.markov_chain(next)
        

    def markov_chain(self, next):
        word_list = []
        for word in range(0, len(self.text) - 1):
            words = []

            for i in range(0, next):
                if word+i in range(0, len(self.text)):
                    words.append(self.text[word+i])
                else:
                    words.append(self.text[word+i - len(self.text)])
                    
            texts = tuple(words)
            word_list.append(texts)

            if word+next in range(0, len(self.text)):
                next_word = self.text[word+next]

            else:
                next_word = self.text[word+next - len(self.text)]

            if texts in self.dictionary.keys():
                dictogram = self.dictionary[texts]
                if next_word:
                    if next_word in dictogram.keys():
                        dictogram.add_count(next_word)
                    else:
                        dictogram.add_count(next_word)
            else:
                if next_word:
                    self.dictionary[texts] = Dictogram([next_word])
        return self.dictionary
    
    def markov_walk(self):
        text = 0
        words = []
        start = random.choice(self.text)
        while text in range(0, 365):
            walk_list = []
            for word in self.markov_dict.keys():
                if start == word[0]:
                    walk_list.append(word)
            if len(walk_list) == 0:
                return words
            randomize = random.choice(walk_list)
            for word in randomize:
                for _ in word:
                    text += 1
                    if text in range(0, 365):
                        continue
                    else:
                        return words
                words.append(word)
                text += 1
            start = self.markov_dict[randomize].sample()
        return words

if __name__ == '__main__':
    markov = MarkovChain(read_source('./data/b99.txt'), 15)
    print(markov.markov_walk())

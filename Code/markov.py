import random

class Markov():
    def __init__(self, word_list):
        self.word_list = word_list.read_source(word_list)
        markov_dict = {}
        word_sequence = range(len(word_list) - 1)
        


            


        





# A Markov chain consists of a bunch of states linked together by transitions telling 
# you how likely it is to go from one state to another.
# To generate a sentence with a Markov chain, we perform a random walk: starting from some 
# state, we pick a random transition (according to its probability), follow it, and repeat. 
# Doing this we visit a sequence of states, which in our application corresponds to a sequence of tokens.

# use functions to create markov -- create class 
# use a dictionary as a start and pass in txt
# iterate/loop over source text/corpus; 
# append

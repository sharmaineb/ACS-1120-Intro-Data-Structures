from dictogram import Dictogram
from histogram import read_souce, generate_histogram
import random







# A Markov chain consists of a bunch of states linked together by transitions telling 
# you how likely it is to go from one state to another.
# To generate a sentence with a Markov chain, we perform a random walk: starting from some 
# state, we pick a random transition (according to its probability), follow it, and repeat. 
# Doing this we visit a sequence of states, which in our application corresponds to a sequence of tokens.

# use functions to create markov -- create class 
# use a dictionary as a start and pass in txt
# iterate/loop over source text/corpus 
# implement tuples
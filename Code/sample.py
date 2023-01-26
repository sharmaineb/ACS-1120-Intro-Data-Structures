import random
from histogram import *
import sys

# stochastic sampling means taking an element from a given collection at random.

# write a function that takes a histogram and returns a single word, at random

def single_word(histogram_dict):
    output = list(histogram_dict.keys())
    output_index = random.randint(0, len(output) - 1)
    random_word = output[output_index]
    return print(random_word)

def word_count(histogram):
    count = 0
    output = random.randint(0, sum(histogram.values()))
    for key, value in histogram.items():
        count += value
        if count >= output:
            return key


if __name__ == "__main__":
    filename = sys.argv[1]
    histo = generate_histogram(filename)
    print(histo)
    print(word_count(histogram_dict))
    
# a word with a higher weighting will have a higher probability of being selected
# frequency weighting: words which appear more frequently in the original text should be more likely
# to be selected by our sampling program.
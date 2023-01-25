import random
from histogram import histogram
import sys

# stochastic sampling means taking an element from a given collection at random.

# write a function that takes a histogram and returns a single word, at random

#  def single_word(histogram):
#     random_word = random.choice()
#     word = random_word[0]
#     return print(word)

def single_word(histogram):
    output = []
    random_word = random.randint(0, len(histogram) -1)
    for word in histogram:
        output.append[word]
    return output[random_word]

# def prob_word(histogram):
#     chosen = random.randint(1, sum(histogram.items()))
#     for word, item in histogram.items():
#         weighted -= item
#         if weighted > chosen:
#             return print(word)


if __name__ == "__main__":
    histogram = histogram("fish_example.txt")
    source_text = sys.argv[1]
    

# a word with a higher weighting will have a higher probability of being selected
# frequency weighting: words which appear more frequently in the original text should be more likely
# to be selected by our sampling program.
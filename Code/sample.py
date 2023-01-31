import random
import sys
from histogram import generate_histogram

# stochastic sampling means taking an element from a given collection at random.

# write a function that takes a histogram and returns a single word, at random

def sample_word(histogram):
    output = random.choices(histogram) # random selection of values from histo
    word = output[0]
    return word

def word_count(histogram):
    count = 0
    output = random.randint(0, sum(histogram.values()))
    for key, value in histogram.items():
        count += value
        if count >= output:
            return key

def output_random(histogram, word_amount):
    random_words = []
    for i in range(word_amount):
        random_words.append(sample_word(histogram))
        output = " ".join(random_words)
    return output

if __name__ == '__main__':
    file = sys.argv[1]
    histogram = generate_histogram("b99.txt")
    print(word_count(histogram))


# a word with a higher weighting will have a higher probability of being selected
# frequency weighting: words which appear more frequently in the original text should be more likely
# to be selected by our sampling program.
    
# a word with a higher weighting will have a higher probability of being selected
# frequency weighting: words which appear more frequently in the original text should be more likely
# to be selected by our sampling program.
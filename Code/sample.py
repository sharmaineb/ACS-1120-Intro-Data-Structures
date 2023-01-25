import random
from histogram import histogram
import sys

# stochastic sampling means taking an element from a given collection at random.

# write a function that takes a histogram and returns a single word, at random

def single_word(histogram):
    output = []
    random_word = random.randint(0, len(histogram)- 1)
    for word in histogram:
        output.append[word]
    return output[random_word]

# def single_word(histogram):
#     all_words = histogram(histogram)
#     random_word = random.choices(
#         list(all_words.items()),
#         weight_words = all_words.values(),
#         k = 1) [0]
#     return random_word

# def single_word(histogram):
#     output = []
#     random_word = random.randint(0, len(histogram) -1)
#     for word in histogram:
#         output.append[word]
#     return output[random_word]

def word_count(histogram):
    random_word = random.randint(1, sum(histogram.items()))
    for word, item in histogram.items():
        random_word -= item
        if random_word > 0:
            continue
        else:
            return word


def prob_word(histogram):
    loopy = {}
    for word in range(10000):
        word = single_word(histogram)
        if word in loopy:
            loopy[word] += 1
        else:
            loopy[word] = 1
    return loopy

if __name__ == "__main__":
    # source_text = "one fish two fish three fish four fish"
    # source_text = histogram("fish_example.txt")
    # # sample = single_word(source_text)
    # # print(sample)
    
    # # prob = prob_word(source_text)
    # # for word in prob:
    # #     print(f"{word}: {prob [word]}")
    # word = histogram(histogram)
    # print(word)
    # word_output = single_word(word)

    # count = prob_word(word)
    # prob_word(word)
    # print(count)

# thank you Andrew A. for the guidance!

# a word with a higher weighting will have a higher probability of being selected
# frequency weighting: words which appear more frequently in the original text should be more likely
# to be selected by our sampling program.
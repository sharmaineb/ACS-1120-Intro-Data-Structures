import random
import sys
from histogram import generate_histogram

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
    histogram = generate_histogram("./data/b99.txt")
    print(word_count(histogram))

import random
import sys

def rearrange_words(set_of_words):
    random.shuffle(set_of_words)
    output = " ".join(set_of_words)
    print(output)


if __name__ == '__main__':
    set_of_words = sys.argv[1:]
    rearrange_words(set_of_words)
import random
import sys

def random_dictionary_words(word_amount, dictionary_file):
    with open(dictionary_file) as file:
        random_words = file.read().splitlines()
        user_input_amount = random.choices(random_words, k=int(word_amount))
        output = " ".join(user_input_amount)
        return print(output)

if __name__ == "__main__":
    random_dictionary_words(int(sys.argv[1]), '/usr/share/dict/words')
    
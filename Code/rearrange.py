import random

def rearrange_words(set_of_words):
    random.shuffle(set_of_words)
    output = " ".join(set_of_words)

    print(output)

if __name__ == '__main__':
    set_of_words = input(str("Enter A List Of Words: ")).split()
    rearrange_words(set_of_words)
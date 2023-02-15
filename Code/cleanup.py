def read_source(filename):
    with open (filename) as text:
        word_list = text.read().split()
    return word_list
# opens and reads file
def read_source(filename):
    with open (filename) as text:
        word_list = text.read().split()
    return word_list
    
# histogram() function that takes a source_text argument
def generate_histogram(word_list):
        histogram = {}
        for word in word_list:
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1
        for key in list(histogram.keys()):
            print(key, ":", histogram[key])
    
        return histogram

# unique_words() function that takes a histogram argument

def unique_words(histogram):
    unique_word_count = len(histogram)
    return unique_word_count

# frequency() function that takes a word and histogram argument
# returns the total count of unique words in the histogram

def frequency(word, histogram):
    frequent_words = histogram[word]
    return frequent_words

# tuple
def histogram_tuple(filename):
    histogram_tuple = []
    with open(filename) as file:
        words = file.read().split()
    for word in range(len(words)):
        histogram_tuple.append((words[word], words.count(words[word])))
    return print(histogram_tuple)

if __name__ == "__main__":
    histogram = generate_histogram("./data/b99.txt")
    print(histogram)
    print(unique_words(histogram))
    histogram_tuple("./data/b99.txt")

    # histogram = generate_histogram("./data/b99.txt")
    # print(histogram)
    # print(unique_words(histogram))
    # histogram_tuple("./data/b99.txt")
    
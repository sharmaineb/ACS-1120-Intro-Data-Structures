# opens and reads file
def read_souce(filename):
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
    histogram = generate_histogram("fish_example.txt")
    print(histogram)
    print(unique_words(histogram))
    histogram_tuple("fish_example.txt")

    # histogram = generate_histogram("book.txt")
    # print(histogram)
    # print(unique_words(histogram))
    # histogram_tuple("book.txt")
    

# attempts:

# def histogram(source_text):
#     histogram_dict = {}
#     with open(source_text) as book_source: 
#         book_content = book_source.read()
#         book_text = book_content.split()
#         for word in book_text:
#             if word in histogram_dict:
#                 histogram_dict[word] += 1
#             else:
#                 histogram_dict[word] = 1
#         return print(histogram_dict)

# for key in histogram:
#     if histogram[key] == 1:
#         unique_word_count += 1
# return len(unique_word_count)
# unique_word_count = 0
# for key in histogram:
#     if histogram[key] == 1:
#         unique_word_count += 1
# return unique_word_count

# if word in histogram.keys():
#     return histogram[word]
# return 0
# for word in histogram.word_count():
#     if word == word:
#         word_frequency = histogram[word]
# if word not in histogram:
#     return("Word Not Found in Histogram.")

# return print(histogram[word])
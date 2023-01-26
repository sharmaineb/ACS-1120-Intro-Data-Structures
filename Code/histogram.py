# histogram() function that takes a source_text argument
histogram_dict = {}

def generate_histogram(filename):
    with open(filename) as file:
        words = file.read().split()
        for word in words:
            if word in histogram_dict:
                histogram_dict[word] += 1
            else:
                histogram_dict[word] = 1
        for key in list(histogram_dict.keys()):
            print(key, ":", histogram_dict[key])
        return print(histogram_dict)

        
# unique_words() function that takes a histogram argument
def unique_words(histogram_dict):
    unique_word_count = len(histogram_dict)
    return unique_word_count
    
# frequency() function that takes a word and histogram argument
# returns the total count of unique words in the histogram
def frequency(word, histogram_dict):
    frequent_words = histogram_dict[word]
    return frequent_words

# tuple
def histogram_book_tuple(filename):
    histogram_book_tuple = []
    with open(filename) as book_content:
        book_text = book_content.read().split()
    for word in range(len(book_text)):
        histogram_book_tuple.append((book_text[word], book_text.count(book_text[word])))
    return print(histogram_book_tuple)
    

if __name__ == "__main__":
    generate_histogram('fish_example.txt')
    unique_words(histogram_dict)
    # generate_histogram("book.txt")
    # generate_histogram_book_tuple("book.txt")

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
# histogram() function that takes a source_text argument
def histogram(source_text):
    histogram_dict = {}
    with open(source_text) as book_source: 
        book_content = book_source.read()
        book_text = book_content.split()
        for word in book_text:
            if word in histogram_dict:
                histogram_dict[word] += 1
            else:
                histogram_dict[word] = 1
        return print(histogram_dict)
        


# unique_words() function that takes a histogram argument
def unique_words(histogram):
    unique_word_count = 0
    for each in histogram.word_count():
        unique_word_count += 1

    return print(unique_word_count)
    


# # frequency() function that takes a word and histogram argument
# # returns the total count of unique words in the histogram
def frequency(word, histogram):
    for word in histogram.word_count():
        if word == word:
            word_frequency = histogram[word]

    return print(word_frequency) 

# tuple
def histogram_book_tuple(source_text):
    histogram_book_tuple = []
    with open(source_text) as book_content:
        book_text = book_content.read().split()
    for word in range(len(book_text)):
        histogram_book_tuple.append((book_text[word], book_text.count(book_text[word])))
    print(histogram_book_tuple)
    return histogram_book_tuple

if __name__ == "__main__":
    histogram("book.txt")
    # histogram_book_tuple("book.txt")

    

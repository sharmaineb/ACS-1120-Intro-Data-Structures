import random

class MarkovChain():
    def __init__(self, word_list):
        self.word_list = self.read_source(word_list)

    def read_source(self, word_list):
        with open(str(word_list)) as text:
            text = text.read().split()
        return text

    def start(self, order):
        texts = self.word_list
        start_texts = []
        for word in range(len(texts) - order):
            if texts[word][0].isupper():
                start_texts.append(tuple(texts[word:word+order]))
        starting_tuple = random.choice(start_texts)
        return ' '.join(starting_tuple)

    def end(self, order):
        texts = self.word_list
        end = []
        for i in range(len(texts) - order):
            if texts[i+order-1][-1] in [".", "?", "!"]:
                texts_end = texts[i:i+order-1]
                ends = texts[i+order-1]
                end.append(" ".join(texts_end + [ends]))
        choices = random.choice(end)
        ends = choices.split()[-1]
        texts_end = choices.split()[:-1]
        return " ".join(texts_end) + " " + ends

    def walk(self, order):
        texts = self.word_list
        markov_dict = {}
        for i in range(len(texts) - order):
            tuples = tuple(texts[i:i+order])
            following_text = texts[i+order]
            if tuples in markov_dict:
                markov_dict[tuples].append(following_text)
            else:
                markov_dict[tuples] = [following_text]
        return markov_dict

    def sentence(self, amount, order):
        markov_dict = self.walk(order)
        start_sentence = self.start(order)
        end_of_sentence = self.end(order)
        sentence = start_sentence.split()
        tuples = tuple(sentence[-order:])
        amount -= len(tuples)

        while len(sentence) < amount:
            try:
                following_text = random.choice(markov_dict[tuples])
            except:
                return " ".join(sentence) + f" {end_of_sentence}"
            
            sentence.extend(following_text.split())
            tuples = tuple(sentence[-order:])
            if tuples == tuple(end_of_sentence.split()):
                break

        return " ".join(sentence) + f" {end_of_sentence}"
                
if __name__ == "__main__":
    word_list = "./data/b99.txt"
    markov = MarkovChain(word_list)
    print(markov.sentence(15, 3))


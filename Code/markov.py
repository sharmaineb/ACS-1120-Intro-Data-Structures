import random

class Markov():
    def __init__(self, word_list):
        self.word_list = self.read_source(word_list)

    def read_source(self, word_list):
        with open(str(word_list)) as text:
            text = text.read().split()
        return text

    def start(self):
        word_list = self.word_list
        words = []
        for word in word_list:
            if word[0].isupper() and word[-1] not in [".", "?", "!"]:
                words.append(word) 
        return random.choice(words)

    def end(self):
        word_list = self.word_list
        words = []
        for word in word_list:
            if word[-1] in [".", "?", "!"]:
                words.append(word)
        return random.choice(words)

    def walk(self):
        words = self.word_list
        markov_dict = {}
        for i in range(len(words) - 1):
            next_word = words[i + 1]
            if words[i] in markov_dict:
                markov_dict[words[i]].append(next_word)
            else:
                markov_dict[words[i]] = [next_word]
        return markov_dict

    def sentence(self, amount):
        markov_dict = self.walk()
        sentence_start = self.start()
        end_of_sentence = self.end()

        sentence = [sentence_start]
        next_word = sentence_start
        amount -= 2 

        for count, _ in enumerate(markov_dict, start=1):
            try:
                next_word = random.choice(markov_dict[next_word])
            except:
                return " ".join(sentence) + f" {end_of_sentence}"

            sentence.append(next_word)
            if next_word == end_of_sentence or count == amount:
                return " ".join(sentence) + f" {end_of_sentence}"
                
if __name__ == "__main__":
    word_list = "./data/b99.txt"
    markov = Markov(word_list)
    print(markov.sentence(15))

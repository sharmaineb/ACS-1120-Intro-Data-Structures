import random

class Markov():
    def __init__(self, word_list):
        self.word_list = self.read_source(word_list)
    
    def read_source(self, word_list):
        with open (word_list) as source_text:
            source_text = source_text.read().split()
        return source_text
    
    def onset(self):
        source_text = self.word_list
        beginning_word = []
        for word in source_text:
            if word[0].isupper() == True:
                beginning_word.append(word)
        return random.choice(beginning_word)
    
    def end(self):
        source_text = self.word_list
        end_word = []
        for word in source_text:
            if word[-1] in [".", "!", "?", ";"]:
                end_word.append(word)
        return random.choice(end_word)

    def markov_walk(self):
        text = self.word_list
        markov_dict = {}
        for index in range(len(text) - 1):
            following_word = text[index + 1]
            if text[index] in markov_dict:
                markov_dict[text[index]].append(following_word)
            else:
                markov_dict[text[index]] = [following_word]
        return markov_dict
    
    def sentence(self, amount):
        walk = self.markov_walk() 
        onset = self.onset()
        end = self.end()

        sentence = [onset]
        following_word = onset
        amount -= 2

        for i, _ in enumerate(walk, start=1):
            try:
                following_word = random.choice(walk[following_word])
            except:
                return " ".join(sentence) + f" {end}"
            sentence.append(following_word)
            if following_word == end or i == amount:
                return " ".join(sentence) + f" {end}"

if __name__ == "__main__":
    text = "./data/b99.txt"
    markov = Markov(text)
    print(markov.sentence(10))

        



        
        


            


        





# A Markov chain consists of a bunch of states linked together by transitions telling 
# you how likely it is to go from one state to another.
# To generate a sentence with a Markov chain, we perform a random walk: starting from some 
# state, we pick a random transition (according to its probability), follow it, and repeat. 
# Doing this we visit a sequence of states, which in our application corresponds to a sequence of tokens.

# use functions to create markov -- create class 
# use a dictionary as a start and pass in txt
# iterate/loop over source text/corpus; 
# append

import random

histogram = [('cats', 3), ('dogs', 4), ('rabbits', 2), ('turtles', 1)]

def sample(histogram):
    """Return a word from this histogram, randomly sampled by weighting each word's 
    probability of being chosen by its observed frequency."""
    tokens = sum([count for word, count in histogram]) # count total tokens
    dart = random.randint(1, tokens) # throw a dart on the number line
    # Note: Assume that randint returns 8 here and dart stores the value 8
    fence = 0 # border of where each word splits the number line
    for word, count in histogram: # loop over each word and its count
        fence += count # move this word's fence border to the right
        if fence >= dart: # check if this word's fence is past the dart
            return word # fence is past the dart, so choose this word
        
        print(f"Word: {word}")
        print(f"Count: {count}")
        print(f"Fence: {fence}")
        

print(sample(histogram))
from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    # your code here
    if word == 'NOUN':
        return random_noun()
    if word == 'VERB':
        return random_verb()
    else:
        return word[0]

print (word_transformer('NOUN'))
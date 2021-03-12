def break_words(stuff):
    """this will break up words for us"""
    words =stuff.split(' ')
    return words

def sorted_words(words):
    """ sort the words"""
    return sorted(words)

def print_first_words(words):
    word = words.pop(0)
    print(word)

def print_last_word(words):
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return sorted_words(words)

def print_first_and_last(sentence): # not working
    print(print_first_words)
    print(print_last_word)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_words(words)
    print_last_word(words)

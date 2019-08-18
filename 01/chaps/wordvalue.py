from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        contents = f.read()
    return [word.strip() for word in contents.splitlines()]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[char.upper()] for char in word if char.isalpha()])

def max_word_value(list_of_words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    words_dict = {calc_word_value(word): word for word in list_of_words}
    return words_dict[max(words_dict.keys())]

if __name__ == "__main__":
    from test_wordvalue import *
    unittest.main()
    pass # run unittests to validate

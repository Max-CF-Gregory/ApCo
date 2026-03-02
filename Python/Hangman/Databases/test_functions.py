from functions import get_word
from functions import guess
import reallycoolhangman

def test_get_word1():
    w = get_word("../two_words.csv")
    assert w in ["hello", "world"]

def test_get_word2():
    w = get_word("../no_words.csv")
    assert w == "no words found in no_words.csv"

def test_new_record_values():
    pass

def test_new_record_values2():
    pass
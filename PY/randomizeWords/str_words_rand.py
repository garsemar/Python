from generate_random_int_list import *
from change_word_order import *


def str_words_rand(list_words, randomized):
    for i in list_words:
        if len(i) <= 3:
            randomized += i + " "
        else:
            list_nums = generate_random_int_list(i)
            rand_word = change_word_order(i, list_nums)
            randomized += rand_word + " "
    return randomized
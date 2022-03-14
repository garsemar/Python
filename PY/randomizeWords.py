from random import *


def generate_random_int_list(word):
    list_nums = []
    pos = 1
    if word[-1] == "," or word[-1] == ".":
        pos = 2
    while len(list_nums) != len(word) - (pos + 1):
        r = randrange(1, len(word) - pos)
        if r not in list_nums:
            list_nums.append(r)
    return list_nums


def change_word_order(word, list_nums):
    rand_word = word[0]
    for j in range(len(list_nums)):
        rand_word += word[list_nums[j]]
    if word[-1] == "," or word[-1] == ".":
        rand_word += word[-2]
    rand_word += word[-1]
    return rand_word


def str_words_rand(list_words, randomized):
    for i in list_words:
        if len(i) <= 3:
            randomized += i + " "
        else:
            list_nums = generate_random_int_list(i)
            rand_word = change_word_order(i, list_nums)
            randomized += rand_word + " "
    return randomized


def randomize_word(words):
    list_words: list = words.split()
    print(list_words)
    randomized = ""
    return str_words_rand(list_words, randomized)


print(randomize_word(input()))

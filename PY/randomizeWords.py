#!/bin/python3

import math
import os
from random import *
import re
import sys


def generate_random_int_list(lenght):
    list_nums = []
    while len(list_nums) != lenght - 2:
        r = randrange(1, lenght - 1)
        if r not in list_nums:
            list_nums.append(r)
    return list_nums


def randomise_word(word):
    # word = list(word)
    rand_word = word[0]
    list_nums = generate_random_int_list(len(word))
    for j in range(len(list_nums)):
        rand_word += word[list_nums[j]]
    rand_word += word[-1]
    return rand_word


if __name__ == '__main__':
    print(randomise_word("campus"))

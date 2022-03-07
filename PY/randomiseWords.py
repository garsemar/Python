#!/bin/python3

import math
import os
from random import *
import re
import sys


def randomiseWords(word):
    word = list(word)
    defWord = [word[0]]
    listNums = []
    while len(listNums) != len(word) - 2:
        r = randrange(1, len(word) - 1)
        if r not in listNums:
            listNums.append(r)
    for j in range(len(listNums)):
        defWord.append(word[listNums[j]])
    defWord.append(word[-1])
    return ''.join(defWord)


if __name__ == '__main__':
    print(randomiseWords("campus"))

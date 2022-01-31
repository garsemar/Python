#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum():
    # Write your code here
    rep = int(input())
    numList = [int(numList) for numList in input().split(" ")]
    print(sum(numList))


if __name__ == '__main__':
    simpleArraySum()

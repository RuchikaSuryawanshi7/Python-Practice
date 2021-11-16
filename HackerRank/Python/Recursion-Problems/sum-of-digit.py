#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def check(no):
    if no < 10:
        return no
    else:
        s = sum([int(x) for x in str(no)])
    return check(s)
def superDigit(n, k):
    s = k * check(int(n))
    return check(s)



first_multiple_input = input().rstrip().split()

n = first_multiple_input[0]

k = int(first_multiple_input[1])

result = superDigit(n, k)
print(str(result) + '\n')


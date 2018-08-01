#!/bin/python3


import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    values = set(a)
    if len(values) == len(a):
        return -1

    distance = min_distance = len(a)
    first = True
    for value in values:
        for elem in a:
            if elem == value:
                if first:
                    first = False
                    distance = 0
                else:
                    if  distance < min_distance:
                        min_distance = distance
                    distance = 0
            distance += 1
        first = True
    return min_distance


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

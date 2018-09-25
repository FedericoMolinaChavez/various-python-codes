#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    counters = dict()
    
    for i in s:
        if(i not in counters):
            counters[i] = 1
        else:
            counters[i] += 1
    c = sorted(counters.values())
    aux1 = c[len(c)-1]-1
    c.pop()
    c.append(aux1)
    print(c)
    first = c[0]
    if(c[0]<c[1]):
        c[0]+=1
    for i in c :
        if i != first:
            return "NO"
    return "YES"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

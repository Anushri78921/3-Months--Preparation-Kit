#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    x=0
    y=0
    z=0
    for i in range(len(arr)):
        if arr[i]==0:
            x=x+1
        elif arr[i]>0:
            y=y+1
        else:
            z=z+1

    p=x/len(arr)
    q=y/len(arr)
    r=z/len(arr)
    print(format(q,'.6f'))
    print(format(r,'.6f'))
    print(format(p,'.6f'))

            
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

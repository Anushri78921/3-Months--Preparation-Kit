#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    total=[]
    for i in range(len(arr)):
        p=arr.pop(i)
        total.append(sum(arr))
        arr.insert(i,p)
         
    x=min(total)
    y=max(total)
    print(x,y)
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

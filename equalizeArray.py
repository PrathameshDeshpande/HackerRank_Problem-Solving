
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    y = []
    l = []
    for i in range(len(arr)):
        c = 0
        for j in range(len(arr)):
            if(j!=i and arr[i]==arr[j]):
                c+=1
                if j not in l:
                    l.append(j)
        if c>0:
            if i not in l:
                l.append(i)
    for q in l:
        y.append(arr[q])
    v = []
    for i in range(len(y)):
        m = 0
        o =0
        for j in range(len(y)):
            if(j!=i and y[i]==y[j]):
                m+=1
                o +=1
        if o > 0:
            m+=1
        if m not in v:
            v.append(m)
    if(len(v)>0):
        return len(arr) - max(v)
    else:
        return len(arr)-1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


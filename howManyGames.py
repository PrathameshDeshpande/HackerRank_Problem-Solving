
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    c = 0
    if(s-p>0):
        s=s-p
        c+=1
    else:
        s = s-p
    while s>0:
        if((p-d)>m and (s-(p-d))>=0 ):
            s=s-(p-d)
            p = p-d
            c+=1
            print(s,c,p)
        elif((m>=(p-d)) and ((s-m)>=0)):
            s=s-m
            c+=1
            print(s,c,p)
        else:
            break
    return c


    # Return the number of games you can buy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()



import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

b = bin(n)

count = 0
tmp = 0
for i in b:
    if i =='1':
        tmp +=1
    else:
        count = max(count,tmp)
        tmp =0

count = max(count,tmp)


print(count)
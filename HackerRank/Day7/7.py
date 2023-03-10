import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

arr_2 = list()

for i in range(len(arr)):
    arr_2.append(arr[len(arr)-1-i])

str_2 = str(arr_2)
str_3 = str()
symb = {'[', ']', ','}
for i in range(len(str_2)):
    if str_2[i] not in symb:
        str_3 +=str_2[i]
print(str_3)
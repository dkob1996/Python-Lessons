import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

i=1

while i<=10:
    print('{} x {} = {}'.format(n, i, n*i))
    i +=1
'''
Complete file with 3 exercises of second python homework
'''
'''
Task 10:
There are n coins on the table. Some of them are tails up, and some are coats of arms. 
Determine the minimum number of coins that need to be turned over so that all the coins are turned up with the same side. 
Print the minimum number of coins to flip
'''
from random import randint
n = int(input("Enter count of coins: "))

# 0 - Heads ; 1 - Tails

count_of_heads = 0
count_of_tails = 0

for i in range(n):
    side_of_the_coin = randint(0, 1)
    # print(side_of_the_coin, end=' ')                             # testing string to see random numbers
    if side_of_the_coin == 0:
        count_of_heads +=1
    else:
        count_of_tails +=1
print()
if count_of_heads>count_of_tails:
    print('We need to return tails, this count: ', count_of_tails)
elif count_of_heads<count_of_tails:
    print('We need to return heads, this count: ', count_of_heads)
elif count_of_heads==count_of_tails:
    print('It is not important what we want to return, because count of heads and tails areh the same: ', count_of_tails)

'''
Task 12:
Petya and Katya are brother and sister. Petya is a student, and Katya is a schoolgirl. Petya helps Katya in math. 
He conceives two natural numbers X and Y (X,Y≤1000), and Katya must guess them. To do this, Petya makes two hints. 
He calls the sum of these numbers S and their product P. 
Help Katya to guess the numbers conceived by Petya.
'''

# Math solivng
'''
s - sum of two numbers
p - multiply of this two numbers


s = x + y
p = x * y
x = p/y
y=s-x -> p= x * y
p = x*(s-x)
p = sx - x*x
x*x + (-sx) +p = 0

D = s*s - 4*1*p
1. D>0    x1=(s+sqrt(D))/2   x2 = (s-sqrt(D))/2   count =2
2. D = 0  x = s/2   count = 1
3. D<0    message - incorrect arguments

if count = 2
y1 = p/x1  y2 = p/x2

if count = 1
y = p/x


'''

from math import sqrt
s = int(input("Enter sum of two numbers: "))
p = int(input("Enter multiply of this two numbers: "))

D = s*s - 4*p

if D > 0:
    x1 = (s+sqrt(D))/2
    x2 = (s-sqrt(D))/2
    y1 = p/x1
    y2 = p/x2
    if (s+sqrt(D)) % 2 > 0 or (s-sqrt(D)) % 2 > 0 or p % x1 > 0 or p % x2 > 0:
        print('Numbers are need to be integer')
    if x1 < 0 or y1 < 0:
        if x2 < 0 or y2 < 0:
            print('Numbers are need to be >0')
        else:
            print('We have one pair of numbers: ')
            print('{0} - first number, {1} - second number'.format(x2, y2))
    elif x2 < 0 or y2 < 0:
        print('We have one pair of numbers: ')
        print('{0} - first number, {1} - second number'.format(x1, y1))
    else:
        print('We have two pairs of numbers: ')
        print('first pair: {0} - first number, {1} - second number'.format(x1, y1))
        print('second pair: {0} - first number, {1} - second number'.format(x2, y2))
elif D == 0:
    x = s/2
    y = p/x
    if s % 2 > 0 or p % x > 0:
        print('Numbers are need to be integer')
    if x < 0 or y < 0:
        print('Numbers are need to be >0')
    else:
        print('We have one pair of numbers: ')
        print('{0} - first number, {1} - second number'.format(x, y))
elif D < 0:
    print('Invalid s and p for solving two numbers (D<0)')

'''
Task 14:
It is required to output all integer powers of two (i.e. numbers of the form 2k) that do not exceed the number N.
'''

n = int(input("Enter number N: "))

from math import log
if n<=0:
    print('Enter, please, n >0')
else:
    grade_of_n = log(n,2)
    count = -1
    print()
    print('All grades of two >=0 and < log(n,2): ')
    while count<int(grade_of_n):
        count +=1
        print(count)

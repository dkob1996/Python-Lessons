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

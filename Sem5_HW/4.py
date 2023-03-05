'''
Task 28: 
Write a recursive function sum(a, b) that returns the sum of two non-negative integers. Of all arithmetic operations, only +1 and -1 are allowed. You can't use loops either.

*Example:*

2 2
    4
'''
def sum(a,b):
    return (sum(a+1,b-1) if b else a)

a = int(input('Enter A: '))
b = int(input('Enter B: '))

print(sum(a,b))
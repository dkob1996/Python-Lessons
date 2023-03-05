'''
Task 26: 
Write a program that takes two numbers A and B as input, and raises the number A to the integer power of B using recursion.

*Example:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
'''
def degree_of_number(a,b):
    if b in [0]:
        return 1
    if b in [1]:
        return a
    if b not in [0,1]:
        return (a*degree_of_number(a,b-1))

a = int(input('Enter number: '))
b = int(input('Enter degree of number: '))

print(degree_of_number(a,b))
'''
1. For a given non-negative integer n, calculate the value of n!. 
N! = 1 * 2 * 3 * ... * N (the product of all numbers from 1 to N) 0! = 1 
Solve the problem using the while loop
Given a natural number A > 1. Determine which Fibonacci number it is,
that is, output a number n such that φ(n) = A.
If A is not a Fibonacci number, print the number -1.
'''
# Factorial

n = int(input("Enter N: "))
fact = 1

while n > 0:
    fact *=  n
    n -= 1

print(fact)


# Fibbonachi

n = int(input())
n0 = 0
n1 = 0
n2 = 1
i = 2                     # Since the first 2 numbers are already known, these are 0 and 1
while n0 < n:
    n0 = n1 + n2
    n1 = n2
    n2 = n0
    i += 1
    if n0 > n:
        i = 0
if i != 0:
    print(i)
else:
    print(-1)
    
'''
2. Tired of the unusually warm winter, residents decided to find out if this is really the longest thaw
in the history of weather observations. They turned to weather forecasters, and they, in turn, engaged
in research statistics for the past years. They are interested in how many days the longest thaw lasted. 
They call a thaw a period in which the average daily temperature exceeded 0 degrees Celsius daily. 
Write a program that helps weather forecasters in their work.

The user enters the number N – the total number of days under consideration (1 ≤ N ≤ 100). 
The following lines contain N integers.

Each number is the average daily temperature on the corresponding day. 
Temperatures are integers and range from -50 to 50

'''
from random import randint
n = int(input("Enter N: "))
count=0

for i in range(n):
    t = randint(-1, 1)
    print(t, end=' , ')
    if t>0:
        count +=1

print()
print('Count of days with thaw:' ,count)

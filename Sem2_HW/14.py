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

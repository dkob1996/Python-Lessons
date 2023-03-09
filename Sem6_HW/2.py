'''
Task 32: 
Determine the indexes of array (list) elements whose values belong to a given range (i.e. not less than a given minimum and not more than a given maximum)
'''

import random
print('Max and min 1-10.')
max_num = int(input('Enter max number: '))
min_num = int(input('Enter min number:'))
list_of_numbers = [random.randint(1, 10) for _ in range(10)]
print(list_of_numbers)

list_of_index = list()

for i in range(len(list_of_numbers)):
    if max_num>=list_of_numbers[i]>= min_num:
        list_of_index.append(i)
print(list_of_index)
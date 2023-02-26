'''
Task 16:
It is required to calculate how many times a certain number X occurs in the array A[1..N]. 
The user enters a natural number N in the first line – the number of elements in the array. 
The following lines contain N integers Ai. The last line contains the number X

*Example:*

5
    1 2 3 4 5
    3
    -> 1

Try to do the task through your algorithm and through the method .count(). Evaluate the speed of work.
'''
# solivng withot random and .count

list_of_numbers = [int(input('Enter numbers: ')) for _ in range(int(input('Enter count of numbers: ')))]
number_to_find = int(input('Enter number to find: '))

count_of_numbers = 0

for i in range(len(list_of_numbers)-1):
    if number_to_find == list_of_numbers[i]:
        count_of_numbers +=1

if count_of_numbers ==0:
    print('Number to find does not exist')
else:
    print(count_of_numbers)


# solivng with .count

list_of_numbers = [int(input('Enter numbers: ')) for _ in range(int(input('Enter count of numbers: ')))]
number_to_find = int(input('Enter number to find: '))

count_of_numbers = list_of_numbers.count(number_to_find)

if count_of_numbers ==0:
    print('Number to find does not exist')
else:
    print(count_of_numbers)

## solving with big data
import random
import time
number_to_find = int(input('Enter number to find: '))
list_of_numbers = [random.randint(1, 10000) for _ in range(10 ** 6)]
# first method without .count

count_of_numbers = 0

start = time.perf_counter()

for i in range(len(list_of_numbers)-1):
    if number_to_find == list_of_numbers[i]:
        count_of_numbers +=1

end = time.perf_counter()
print(end - start)
a = end-start

# second method .count
start = time.perf_counter()

count_of_numbers = list_of_numbers.count(number_to_find)

end = time.perf_counter()
print(end - start)
b = end-start

if count_of_numbers ==0:
    print('Number to find does not exist')
else:
    print(count_of_numbers)

print('difference beetwen without .count and with: ', a/b)
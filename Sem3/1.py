# find max in list
'''
some_list = [1,2,3,4,10,3,20,3,4,7]

maxx =0
for i in range(0,len(some_list)):
    if some_list[i]>some_list[maxx]:
        maxx=i
print(maxx)
'''
# find count of numbers and then numbers, find average arephmetic even numbers
'''
# first variant
count = int(input('Enter cound of numbers: '))
some_list=[]
for i in range(count):
    n = int(input())
    some_list.append(n)
print(some_list)

# second variant
print([int(input()) for _ in range(int(input('Enter count of numbers: ')))])
'''

# tuple
import sys
import random
'''
some_list = [0] *10 **6
some_tuple = tuple(some_list)
print(sys.getsizeof(some_list))    # size of memory some_list
print(sys.getsizeof(some_tuple))
'''
# sets
'''
some_set = set()
for _ in range(10**6):
    some_set.add(random.randint(1,1000))

some_list = [random.randint(1,1000) for _ in range(10**6)]   # 10**6
some_set = {random.randint(1,1000) for _ in range(10**6)}    # 1000 

some_set = {random.randint(1,1000) for _ in range(1000)}     # 636 <1000 without duplicate
'''
import time
'''
some_list = [random.randint(1,1000) for _ in range(10**6)]   # 
some_set = {random.randint(1,10**9) for _ in range(10**6)}    # 

find_number =6 

start = time.perf_counter()
print(find_number in some_list)
end = time.perf_counter()
a = end-start
print(end-start)

start = time.perf_counter()
print(find_number in some_set)
end = time.perf_counter()
b = end-start
print(end-start)

print(a/b)
'''
# differenece beetwen list and set about speed
'''
some_list=[]
count=0
for _ in range(10**6):
    some_list.append(count)
    count +=1

some_set=set()
count=0
for _ in range(10**6):
    some_set.add(count)
    count +=1

find_number = 999998
start = time.perf_counter()
print(find_number in some_list)
end = time.perf_counter()
a = end - start

start = time.perf_counter()
print(find_number in some_set)
end = time.perf_counter()
b = end - start
print(a / b)
'''

# dictionary
a=0
print(id(a))  # id memory for object a


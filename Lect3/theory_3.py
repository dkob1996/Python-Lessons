# Functions - def

# def function_name(x):
    # body line 1
    # body line n
    # optional return

# Exercise for functions
# We need to create function - sumNumbers(n), which will calculate summ all elements from 1 to n.
'''
def sumNumbers(n):
    summa=0
    for i in range(1, n+1):
        summa +=i
    print(summa)

sumNumbers(5)

def sumNumbers(n):
    summa=0
    for i in range(1, n+1):
        summa +=i
    return summa

print(sumNumbers(5))

def sumNumbers(n):
    summa=0
    for i in range(1, n+1):
        summa +=i
    return summa

a = sumNumbers(5)
print(a)

def sumNumbers(n, y = 'Hello'):
    print(y)
    summa=0
    for i in range(1, n+1):
        summa +=i
    return summa

a = sumNumbers(5)
print(a)

# Function with unlimited counts of arguments (*args)
def sum_str(*args):
    res=''
    for i in args:
        res +=i
    return res

print(sum_str('q', 'e', 'l'))

# Modules from module.py
import module

print(module.max1(5,9))

#
from module import max1

print(max1(5,9))

#
from module import *   # * - import all functions from module

print(max1(5,9))

#
import module as m1   # change name of module in this file

print(m1.max1(5,9))
'''

#Recurtion
# Exercise Fibbonachi
'''
def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1)+fib(n-2)
'''
'''
from module import fib

list_1 = []
for i in range(1,10):
    list_1.append(fib(i))
print(list_1)
'''

# Algoritms
'''
def QuickSort(array):
    if len(array)<=1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return QuickSort(less) + [pivot] + QuickSort(greater)
'''
'''
from module import QuickSort

print(QuickSort([14,5,9,6,3,58,7,5,2,7]))
'''
'''
def MergeSort(nums):
    if len(nums) > 1:
        mid = len(nums) //2
        left = nums[:mid]
        right = nums[mid:]
        MergeSort(left)
        MergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
'''
from module import MergeSort
list_1 = [14,5,9,6,3,58,7,5,2,7]
MergeSort(list_1)
print(list_1)
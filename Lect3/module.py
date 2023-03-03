# Find Max
def max1(a,b):
    if a>b:
        return a
    return b

# Fibbonachi
def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1)+fib(n-2)

# Sort from max to min
def QuickSort(array):
    if len(array)<=1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return QuickSort(less) + [pivot] + QuickSort(greater)

# Sort form max to min through devide list
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
'''
Task 22: 
Two unordered sets of integers are given (maybe with repetitions). 
Output without repetition in ascending order all the numbers that occur in both sets.
The user enters 2 numbers. n is the number of elements of the first set. m is the number of elements of the second set. 
Then the user enters the elements of the sets themselves. (Try using sets and their intersection)
'''

n_numbers = {int((input('Enter numbers n: '))) for _ in range(int(input('Enter count of numbers n:')))}
m_numbers = {int((input('Enter numbers m: '))) for _ in range(int(input('Enter count of numbers m:')))}

inter = n_numbers.intersection(m_numbers)

print(sorted(inter))

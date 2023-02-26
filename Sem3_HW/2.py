'''
Task 18:
It is required to find in the array A[1..N] the element closest in magnitude to a given number X. 
In the first line, the user enters a natural number N – the number of elements in the array. 
The following lines contain N integers Ai. The last line contains the number X

*Example:*

5
    1 2 3 4 5
    6
    -> 5
'''
list_of_numbers = [int(input('Enter numbers: ')) for _ in range(int(input('Enter count of numbers: ')))]
number_to_find = int(input('Enter number to find: '))

list_of_count = list()

for i in range(len(list_of_numbers)):
    flag = False
    if list_of_numbers[i] - number_to_find < 0:
        list_of_count.append(number_to_find-list_of_numbers[i])
    if list_of_numbers[i] - number_to_find > 0:
        list_of_count.append(list_of_numbers[i] - number_to_find)
    if list_of_numbers[i] - number_to_find == 0:
        print('Find element with 0 difference: index - {0}, number - {1}'.format(i, list_of_numbers[i]))
        list_of_count.append(0)
        flag = True
        break
if not flag:
    min =0
    for i in range(len(list_of_count)):
        if list_of_count[i]<list_of_count[min]:
            min=i
    print('Most closer number', list_of_numbers[min])
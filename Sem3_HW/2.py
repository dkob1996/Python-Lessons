'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

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
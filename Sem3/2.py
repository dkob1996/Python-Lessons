# 1. 
# Дан список чисел. 
# Определите, сколько в нем встречается различных чисел.

# 2. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо, K – положительное число.

# 3. 
# Напишите программу для печати всех уникальных значений в словаре.

# 4. 
# Дан массив, состоящий из целых чисел. Напишите программу, 
# которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)

# 5.
'''
Формат ввода
Вводится количество играющих, затем строки, в которых могут быть их имена. Затем вводится количество имен и сами имена детей для поиска.

Формат вывода
Для каждого имени выведите номер строки (счет с 1), в которой оно первый раз встретилось, или -1, если такого имени не было.
7
Bessy kept the garden gate,
And Mary kept the pantry.
Little Betty Blue Lost her holiday shoe.
Billy, Billy, come and play.
Yes, my Polly, so I will.
Little Bobby Snooks was fond of his books.
Robert Barnes, my fellow fine, can you shoe this horse of mine?
4
Mary
Jack
Billy
Bobby

Вывод:
2
-1
4
6
'''



#1
'''
some_list=[1,2,3,2,1,5,78,8,4]

some_set=set(some_list)
print(len(some_set))
'''

#2
'''
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
'''
'''
list_1 = [int(input('Enter numbers one to second: ')) for _ in range(int(input('Enter N numbers: ')))]
print(list_1)

k = int(input('Enter some number: '))
other_list=list_1[k:] + list_1[:k]
print(other_list)
'''

# 3
'''
new_dict = {1: 3, 2: 4, 5: 38, 22: 3}

print(new_dict.values())
a = new_dict.values()
new_set = set(a)
print(new_set )

#some_set = set(new_dict)
#print(some_set)
'''

# 4
'''
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
'''
'''
our_list = [int(input('enter element: ')) for _ in range(int(input('enter cound of elements: ')))]

count =0
for i in range(0,len(our_list)-1):
    if  our_list[i+1] > our_list[i]:
        count +=1
print(count)
'''

# 5

list_of_strigs = [input('enter string: ') for _ in range(int(input('enter count of string: ')))]
list_of_names = [input('enter names: ') for _ in range(int(input('enter count of names: ')))]

for i in range(0, len(list_of_names)):
    flag = False
    for j in range(0, len(list_of_strigs)):
        if list_of_names[i] in list_of_strigs[j]:
            print(j+1)
            flag = True
            break

    if not flag:
        print(-1)
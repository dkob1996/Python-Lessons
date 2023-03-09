'''
Задача 30:  
Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''
first_element = int(input('Enter first element: '))
difference = int(input('Enter difference: '))
count_of_elem = int(input('Enter count of elements: '))

list_of_el =list()
i = 0
while i<count_of_elem:
    tmp = first_element + (i)*difference
    list_of_el.append(tmp)
    i +=1
print(list_of_el)

'''
### Задача 32: 
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
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

'''
Задача 33: 
Для введенных строк определите, в какой из них встречается больше всего различных символов, отличающихся от контрольного. 
Выведите эти символы из строки без повторений, каждый с новой строки. Если таких строк несколько, выведите символы из любой.

Формат ввода
Вводится контрольный символ, затем количество строк, затем сами строки.

Формат вывода
Выведите подряд без повторений символы из строки, в которой их оказалось больше всего, не считая контрольный. 
Если ни одной не оказалось, выведите -1. Порядок вывода произвольный.

Пример 1
Ввод

E
5
EVERY
MAN
TO
HIS
TASTE

Вывод
RVY

Пример 2
Ввод

A
4
AA
AAA
AAAA
AAAAAA

Вывод
-1
'''
control = input('Enter control symbol: ')
list_of_str = [input('Enter string: ') for _ in range(int(input('Enter count of strings: ')))]

#control = 'E'
#list_of_str = ['EVERYS', 'MAN', 'TO', 'HIS', 'TASTE']

str_set = set(list_of_str)

d = {}

for i in str_set:
    tmp =0
    str_tmp = str()
    used_set = set(control)
    for j in range(len(i)):
        if i[j] not in used_set:
            used_set.add(i[j])
            tmp +=1
            str_tmp +=i[j]
    d[str_tmp] = tmp

max_el = 0
max_str = str()
for item in d:
    if d[item]>max_el:
        max_el = d[item]
        max_str = item

if max_el >0:
    print(max_str)
else:
    print(-1)
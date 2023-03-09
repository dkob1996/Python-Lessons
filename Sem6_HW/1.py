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
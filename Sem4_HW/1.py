'''
Задача 22: 
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств. (Попробуйте использовать множества и их пересечение)
'''

n_numbers = {int((input('Enter numbers n: '))) for _ in range(int(input('Enter count of numbers n:')))}
m_numbers = {int((input('Enter numbers m: '))) for _ in range(int(input('Enter count of numbers m:')))}

inter = n_numbers.intersection(m_numbers)

print(sorted(inter))

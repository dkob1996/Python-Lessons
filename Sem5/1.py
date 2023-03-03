# default def
'''
def hello(name='unknwon'):
    print('Hello', name)


hello(input('Enter your name: '))

# def with unlimited
def hello(*name_list):
    for name in name_list:
        print('Hello', name)

hello = ('Alex', 'Ann', 'Sergey')

# def with dictionary
def hello(**info):
    for key, value in info.items():
        print(key, value)

hello(name='Alex', surname='Salnikov', age=21)
'''
'''
1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где

a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

Требуется найти N-е число Фибоначчи
'''
# recurtion
'''
import time
start = time.perf_counter()
def fib(n):
    if n in [0]:
        return 0
    if n in [1]:
        return 1
    return fib(n-1)+fib(n-2)
end = time.perf_counter()
list_1 = []
n1 = int(input('Enter N: '))
for i in range(0,n1+1):
    list_1.append(fib(i))
print(list_1[n1])
a = end-start
# not recurtion
start = time.perf_counter()
def fib(N):
    a_cur = 1
    a_prev = 1
    a_prev_early = 0

    for i in range(2, N):
        a_prev_early = a_prev
        a_prev = a_cur
        a_cur = a_prev_early + a_prev

    return a_cur
end = time.perf_counter()
b = end-start

N = int(input("Введите число N: "))

print(fib(N))

print(a/b)
'''

# factorial
'''
def fact(n):
    if n ==0:
        fact=0
    if n ==1:
        fact=1     # do later
    


fact = 1
for i in range(2,31):
    fact *=i
print(fact)
'''

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
#  5, 5, 4, 2, 3, 4, 5 -> 2, 2, 4, 2, 3, 4, 2
'''
def seracher(marks):
    max_number =marks[0]
    min_number =marks[0]
    for i in marks:
        if i<min_number:
            min_number = i
        if i>max_number:
            max_number = i
    return min_number, max_number

def changer(*marks):
    res = seracher(marks)
    our_min, our_max = res[0], res[1]
    marks = list(marks)

    for i in range(len(marks)):
        if marks[i]==our_max:
            marks[i] = our_min
    return marks

print(changer(5, 5, 4, 2, 3, 4, 5))
'''
'''
# 1. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)*

def finder(number):
    for i in range(2,(number//2)+1):
        if number % i ==0:
            return 'Not Simple'
        
    return 'Simple'

result = finder(int(input('Enter number: ')))
print(result)
'''
'''
Заданы три множества идентификаторов – человек болел, сделал 2 прививки, имеет медотвод. Если его идентификатор есть хотя бы в одном из множеств, то ему нужно выдать QR-код.

Напишите программу, которая будет это проверять.

Формат ввода
Три раза вводятся числа (идентификаторы), пока не будет введена пустая строка. Затем вводится количество запросов и сами запросы.

Формат вывода
Вывести все запросы (по одному в строке), которые есть хотя бы в одном из множеств, без повторений, порядок вывода произвольный.
'''
'''
123
231
301

301
200

222
212

3
221
123
301
Вывод:
123
301
'''
#ill_set = set()
#inj_set = set()
#paper_set = set()
big_set = set()
for _ in range(3):
    while True:
        id = input(': ')
        if not id:
            break
        big_set.add(id)

number = int(input('Enter count of id: '))
for _ in range(number):
    find_id = input('id: ')
    if find_id in big_set:
        print(find_id)
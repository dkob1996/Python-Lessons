'''
## Задача 1
Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.
Пример
Ввод

8-5+2-1
Вывод
4

-5+3+8-7
-1
'''


equal = input('Введите ваше уравнение: ')

str_numbers = ['0','1','2','3','4','5','6','7','8','9']


def sum_with_1_st_plus(equal,number):
    for i in range(len(equal)-1):
        if equal[i] =='+':
            number+=int(equal[i+1])
        if equal[i] =='-':
            number -= int(equal[i+1])
    return number

def sum_with_1_st_minus(equal,number):
    for i in range(1,len(equal)-1):
        if equal[i] =='+':
            number+=int(equal[i+1])
        if equal[i] =='-':
            number -= int(equal[i+1])
    return number


if equal[0] in str_numbers:
    number =int(equal[0])
    print(sum_with_1_st_plus(equal,number))
if equal[0] not in str_numbers:
    number = 0-int(equal[1])
    print(sum_with_1_st_minus(equal,number))


'''
Задача 2
Словом в данной задаче считается последовательность букв, ограниченная пробелами или началом или концом строки.
Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)

Формат ввода
Вводится строка.

Формат вывода
Выведите слова из строки по одному.

Пример 1
Ввод

Hello, world!
Вывод
Hello,
world!
Пример 2
Ввод

My heart in the Highland
Вывод
My
heart
in
the
Highland
'''
str_phrase=input('Введите вашу строку: ')

str_one =str()
k=0

for i in range(len(str_phrase)):
    if str_phrase[i] != ' ':
        str_one +=str_phrase[i]
    if str_phrase[i] == ' ':
        k+=1
        print(str_one)
        str_one=str()

print(str_one)


'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
'''
def degree_of_number(a,b):
    if b in [0]:
        return 1
    if b in [1]:
        return a
    if b not in [0,1]:
        return (a*degree_of_number(a,b-1))

a = int(input('Введите число: '))
b = int(input('Введите степень числа: '))

print(degree_of_number(a,b))

'''
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4 
'''
def sum(a,b):
    return (sum(a+1,b-1) if b else a)

a = int(input('Введите A: '))
b = int(input('Введите B: '))

print(sum(a,b))
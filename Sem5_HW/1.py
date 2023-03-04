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


equal = input('Enter your equal: ')

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
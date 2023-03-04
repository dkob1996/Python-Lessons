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
str_phrase=input('Enter your string: ')

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

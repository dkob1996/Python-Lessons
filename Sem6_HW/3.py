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

d = {}

for i in list_of_str:
    tmp =0
    str_tmp = str()
    for j in range(len(i)):
        if i[j] not in control:
            tmp +=1
            str_tmp +=i[j]
    d[str_tmp] = tmp

print(d)

#empt_str = str()

for (i,j) in d.items():
    max_el = j
    if j+1>max_el:
        max_el =j+1
        print(max_el)
        #empt_str = i
#print(d[empt_str])

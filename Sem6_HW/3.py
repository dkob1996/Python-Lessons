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
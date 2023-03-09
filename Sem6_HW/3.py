'''
Task 33: 
For the entered strings, determine which of them contains the most different characters that differ from the control one. Print these characters from the string without repetition, each from a new line. If there are several such lines, output characters from any one.

Input format
A control character is entered, then the number of lines, then the lines themselves.

Output format
Print in a row, without repetition, the characters from the string in which there were most of them, not counting the control one. If there were none, print -1. The order of output is arbitrary.

Example 1
Input

E
5
EVERY
MAN
TO
HIS
TASTE


RVY output

Example 2
Input

A
4
AA
AAA
AAAA
AAAAAA

Output
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
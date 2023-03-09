### Task 30:  
Fill the array with arithmetic progression elements. 
Its first element, the difference and the number of elements must be entered from the keyboard. 
The formula for obtaining the nth term of the progression is: an = a1 + (n-1) * d.
Each number is entered from a new line.

### Task 32: 
Determine the indexes of array (list) elements whose values belong to a given range (i.e. not less than a given minimum and not more than a given maximum)

### Task 33: 
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


## Translation:<br>
### Задача 30:  
Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

### Задача 32: 
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

### Задача 33: 
Для введенных строк определите, в какой из них встречается больше всего различных символов, отличающихся от контрольного. Выведите эти символы из строки без повторений, каждый с новой строки. Если таких строк несколько, выведите символы из любой.

Формат ввода
Вводится контрольный символ, затем количество строк, затем сами строки.

Формат вывода
Выведите подряд без повторений символы из строки, в которой их оказалось больше всего, не считая контрольный. Если ни одной не оказалось, выведите -1. Порядок вывода произвольный.

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
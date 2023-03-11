### Task 34:  
Winnie the Pooh asked you to see if there is a rhythm in his poems. Since it is not so easy to understand his chants, how easily he comes up with them, you should write a program. Winnie-the-Pooh believes that there is a rhythm if the number of syllables (i.e. the number of vowel letters) in each phrase of the poem is the same. A phrase can consist of one word, if there are several words in the phrase, then they are separated by hyphens. Phrases are separated from each other by spaces. The poem Winnie-the-Pooh drives into the program from the keyboard. In the answer, write “Pam pam pam” if the rhythm is all right and “Pam param”, if the rhythm is not all right

*Example:*

*Input:* para-ra-ram ram-pam-papam pa-ra-pa-da    
    *Output:* Pam pam pam  

### Task 36: 
Write a function print_operation_table(operation, num_rows=6, num_columns=6), which takes as an argument a function that calculates an element by row and column number. The num_rows and num_columns arguments specify the number of rows and columns of the table to be printed. The numbering of rows and columns starts from one (think about why not from zero). Note: A binary operation is any operation that has exactly two arguments, as, for example, a multiplication operation.

*Example:*

*Input:* `print_operation_table(lambda x, y: x * y) ` <br>
*Output:*
1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36

### Translation:

### Задача 34:  
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

*Ввод:* пара-ра-рам рам-пам-папам па-ра-па-да    
    *Вывод:* Парам пам-пам  

### Задача 36: 
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

*Пример:*

*Ввод:* `print_operation_table(lambda x, y: x * y) ` <br>
*Вывод:*
1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
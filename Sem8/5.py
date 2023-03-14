# Дан текстовый файл с некоторым количеством строк, в каждой из которых записано целое число.
# Вводится число, нужно найти такие числа из файла, которые в сумме дают вводимое число.

with open('Sem8/5_info.txt', 'r', encoding='utf-8') as file:
        line_1 = file.read().splitlines()
        print(line_1)
        count = 0
        number = int(input('Enter number: '))
        for i in range(len(line_1)):
            for j in range(i+1, len(line_1)):
                  if (int(line_1[i])+int(line_1[j])) ==number:
                        print(int(line_1[i]), int(line_1[j]))

# Дан текстовый файл, вывести список из предпоследних слов в строках, индексы которых кратны 3, если в строке 1 слово,
# то выводим -1.
# Результаты вывести в файл res.txt

#input_file = input('Введите название файла: ')
with open('Sem8/3_info.txt', 'r', encoding='utf-8') as file:
#    symb = input('Enter find symbol: ')
#    count = 0
    text = file.read().splitlines()
    for i in range(len(text)):
        if i % 3==0:
            some_list = text[i].split()
            if len(some_list) > 1:
                print(some_list[-2])
            else:
                print(-1)
        else:
            print(0)

#print(text)
#with open('Sem8/res.txt', 'w', encoding='utf-8') as file:
#        file.write(str(count))


'''
name = input('Enter file name: ')
with open(name, 'r', encoding='utf-8') as file:
    with open('res.txt', 'w', encoding='utf-8') as res:
        text = file.read().splitlines()
        for i in range(len(text)):
            if i % 3 == 0:
                a = text[i].split()
                if len(a) > 1:
                    res.write(a[-2] + '\n')
                else:
                    res.write('-1' + '\n')
            else:
                res.write('0' + '\n')
'''
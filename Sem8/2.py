# Пользователь вводит название файла и символ, найти количество таких символов в файле и результат записать в файл res.txt
input_file = input('Введите название файла: ')
with open(input_file, 'r', encoding='utf-8') as file:
    symb = input('Enter find symbol: ')
    count = 0
    text = file.read()

    print(text.count(symb))        # можно использовать встроенный метод - он быстрее

    for letter in text:
        if letter == symb:
            count +=1
    print(count)

with open('Sem8/res.txt', 'w', encoding='utf-8') as file:
        file.write(str(count))
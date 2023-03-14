### Чтение
# вывод текста из файла
with open('1_info.md', 'r', encoding='utf-8') as file:
    text = file.read()
    print(text)

# вывод слов из файла
with open('1_info.md', 'r', encoding='utf-8') as file:
    text = file.read()
    for letter in text:
        print(letter)

# вывод строчек чтобы не перегружать оперативную память
with open('1_info.md', 'r', encoding='utf-8') as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()

# вывод строчек в списке
with open('1_info.md', 'r', encoding='utf-8') as file:
    text = file.read().splitlines()       # text = file.readlines()
    print(text)

### Запись
## Перезапись
# Запись в строчку
with open('1_info.md', 'w', encoding='utf-8') as file:
    res = [1,2,3,4]
    for el in res:
        file.write(str(el))

# Запись в столбик
with open('1_info.md', 'w', encoding='utf-8') as file:
    res = [1,2,3,4]
    for el in res:
        file.write(str(el)+'\n')

## Дозапись
with open('1_info.md', 'a', encoding='utf-8') as file:
    res = [1,2,3,4]
    for el in res:
        file.write(str(el))
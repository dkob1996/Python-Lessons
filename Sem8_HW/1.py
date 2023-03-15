'''
### 1: 
Напишите функцию read_last(lines, file), которая будет открывать определенный файл file 
и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, 
что задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым:
'''
def read_last(lines,file):
    with open(file, 'r', encoding='utf-8') as res:
        text = res.read().splitlines()
        count =-1
        if lines <1:
            print('Low count of words')
        else:
            for i in range(len(text)):
                some_list = text[i].split('\n')
                for j in range(len(some_list)):
                    #print(i)
                    word = some_list[j].split()
                    count +=1
                    if count < lines:
                        print(word[len(word)-1])
                    else:
                        break

words = int(input('Enter count of words: '))
file_path = input('Enter path of file: ')     # 'Sem8_HW/article.txt'
a = read_last(words,file_path)
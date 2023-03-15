'''
### 2: 
Требуется реализовать функцию longest_words(file), которая записывает в файл result.txt слово, 
имеющее максимальную длину (или список слов, если таковых несколько).
'''
def longest_words(file):
    with open(file, 'w', encoding='utf-8') as res:
        with open('Sem8_HW/article.txt', 'r', encoding='utf-8') as file:
            line_1 = file.read().splitlines()
            word = list()
            for i in range(len(line_1)):
                some_list = line_1[i].split('\n')
                for j in range(len(some_list)):
                    word += some_list[j].split()
            
            count_list =[]

            for i in word:
                count = 0
                for j in range(len(i)):
                    count +=1
                count_list.append(count)
            
            max = 0
            max_list = []
            for i in range(len(count_list)):
                if count_list[i] > max:
                    max = count_list[i]
                    max_list = []
                    max_list.append(word[i])
                elif count_list[i] == max:
                    max_list.append(word[i])

            for i in max_list:
                res.write(str(i))
                res.write('\n')

words = input('Enter path of file: ')    # Sem8_HW/result.txt
a = longest_words(words)
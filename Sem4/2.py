# 27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки. Определите, сколько различных
# слов содержится в этом тексте.

a = 'слова считаются словами  если. мы правы! слова если'
words = set()
word = ''
for i in a: 
    if i not in {' ', '.','!', '?'}:
        word += i
    else: 
        if word != '':
            words.add(word)
        word = ''
print(len(words))


a_list = a.split()
b_list = a_list.split('!')
print(len(set(b_list)))

# задача 22 - множества и фор
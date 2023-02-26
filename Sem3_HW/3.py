'''
Task 20:
In the board game Scrabble, each letter has a certain value. In the case of the English alphabet, points are distributed as follows: 
A, E, I, O, U, L, N, S, T, R – 1 point; D, G – 2 points; B, C, M, P – 3 points; F, H, V, W, Y – 4 points; K – 5 points; J, X – 8 points; Q, Z – 10 points. 

And Russian letters are evaluated as follows: 
А, В, Е, И, Н, О, Р, С, Т – 1 point; Д, К, Л, М, П, У – 2 points; Б, Г, Ё, Ь, Я – 3 points; Й, Ы – 4 points; Ж, З, Х, Ц, Ч – 5 points; Ш, Э, Ю – 8 points; Ф, Щ, Ъ – 10 points.

Write a program that calculates the cost of the word entered by the user. 
We will assume that only one word is submitted to the input, which contains either only English or only Russian letters.

*Example:*

ноутбук
    12
ERROR
    5
'''
# A, E, I, O, U, L, N, S, T, R – 1 point; 
# А, В, Е, И, Н, О, Р, С, Т – 1 point; 
dictionary1 = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
               'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 's': 1, 't': 1, 'r': 1}
dictionary1RU = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
                 'а': 1, 'в': 1, 'е': 1, 'и': 1, 'н': 1, 'о': 1, 'р': 1, 'о': 1, 'т': 1}
# D, G – 2 point;
# Д, К, Л, М, П, У – 2 point; 
dictionary2 = {'D': 2, 'G': 2,
               'd': 2, 'g': 2}
dictionary2RU = {'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
                 'д': 2, 'к': 2, 'л': 2, 'м': 2, 'п': 2, 'у': 2}
# B, C, M, P – 3 point; 
# Б, Г, Ё, Ь, Я – 3 point;
dictionary3 = {'B': 3, 'C': 3, 'M': 3, 'P': 3,
               'b': 3, 'c': 3, 'm': 3, 'p': 3}
dictionary3RU = {'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
                 'б': 3, 'г': 3, 'ё': 3, 'ь': 3, 'я': 3}
# F, H, V, W, Y – 4 point;
# Й, Ы – 4 point;
dictionary4 = {'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
               'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4}
dictionary4RU = {'Й': 4, 'Ы': 4,
                 'й': 4, 'ы': 4}
# K – 5 point; 
# Ж, З, Х, Ц, Ч – 5 point; 
dictionary5 = {'K': 5,
               'k': 5}
dictionary5RU = {'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
                 'ж': 5, 'з': 5, 'ч': 5, 'ц': 5, 'ч': 5}
# J, X – 8 point;
# Ш, Э, Ю – 8 point;
dictionary8 = {'J': 8,'X': 8,
               'j': 8,'x': 8}
dictionary8RU = {'Ш': 8, 'Э': 8, 'Ю': 8,
                 'ш': 8, 'э': 8, 'ю': 8}
# Q, Z – 10 point. 
# Ф, Щ, Ъ – 10 point.
dictionary10 = {'Q': 10,'Z': 10,
                'q': 10,'z': 10}
dictionary10RU = {'Ф': 10, 'Щ': 10, 'Ъ': 10,
                  'ф': 10, 'щ': 10, 'ъ': 10}

alphabet = ["А","Б","В","Г","Д","Е","Ё","Ж","З","И","Й","К","Л","М","Н","О",
            "П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я"
            "а","б","в","г","д","е","ё","ж","з","и","ё","к","л","м","н","о",
            "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]

word = input('Enter your word: ')

list_of_RU_index = list()
list_of_EN_index = list()

countRU =0
countEN=0

for i in range(len(word)):
    if word[i] in alphabet:
        countRU +=1
        list_of_RU_index.append(i)
    if word[i] not in alphabet:
        countEN +=1
        list_of_EN_index.append(i)

if len(word) == countRU and len(word) !=countEN:
    dictionary = dictionary1RU | dictionary2RU | dictionary3RU | dictionary4RU | dictionary5RU | dictionary8RU | dictionary10RU
    flag = True
if len(word) == countEN and len(word) !=countRU:
    dictionary = dictionary1 | dictionary2 | dictionary3 | dictionary4 | dictionary5 | dictionary8 | dictionary10
    flag = True
if len(word) != countRU and len(word) != countEN:
    flag = False

score =0
if flag ==True:
    for i in range(len(word)):
        if word[i] in dictionary:
            score += dictionary[word[i]]
    print('Score: ',score)
if not flag:
    print('You should correct your word')
    print('Positions of Englis letters: ',list_of_EN_index)
    print('Positions of Russian letters: ',list_of_RU_index)

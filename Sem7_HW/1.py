'''
Task 34:  
Winnie the Pooh asked you to see if there is a rhythm in his poems. 
Since it is not so easy to understand his chants, how easily he comes up with them, you should write a program. 
Winnie-the-Pooh believes that there is a rhythm if the number of syllables (i.e. the number of vowel letters) in each phrase of the poem is the same. 
A phrase can consist of one word, if there are several words in the phrase, then they are separated by hyphens. 

Phrases are separated from each other by spaces. The poem Winnie-the-Pooh drives into the program from the keyboard. 

In the answer, write “Pam pam pam” if the rhythm is all right and “Pam param”, if the rhythm is not all right

*Example:*

*Input:* para-ra-ram ram-pam-papam pa-ra-pa-da    
    *Output:* Pam pam pam  
'''
main_set = set()
main_set = {'а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я'}

phrase = input('Enter your phrase: ')
#phrase = 'пара-ра-рам рам-пам-папам па-ра-па-да'

def find_count(words, phr):
    count =0
    for i in phr:
        if i in words:
            count +=1
    return count

def answer(count):
    if count %2 ==0:
        print('Парам пам-пам')
        print('ok')
    else:
        print('Пам парам')
        print('not ok')


count_of_words = find_count(main_set,phrase)
answer_of_quest = answer(count_of_words)

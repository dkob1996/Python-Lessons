'''
39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), 
которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
Затем число M - количество элементов во втором массиве. Затем элементы второго массива
'''
list_1 =[int(input('Enter elements: ')) for _ in range(int(input('Enter count of elements: ')))]
list_2 ={int(input('Enter elements: ')) for _ in range(int(input('Enter count of elements: ')))}

for i in list_1:
    if i not in list_2:
        print(i)
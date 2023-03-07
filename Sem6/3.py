'''
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
Вводится список чисел. Все числа списка находятся на разных строках.
# 3 3 4 5 6 3 -> 1
# 3 3 4 5 3 6 3 -> 2
# 3 3 4 4 5 5 3 1 6 3 -> 4
'''
# 1st solving
list_1 = [int(input('Enter N elements: '))
          for _ in range(int(input('Enter count of N elements: ')))]

used_set = set()

amount = 0
for el in list_1:
    if el not in used_set:
        amount +=list_1.count(el) //2
        used_set.add(el)

print(amount)


# Second solving

list_1 = [int(input('Enter N elements: '))
          for _ in range(int(input('Enter count of N elements: ')))]

count_dict ={}

for el in list_1:
    if el not in count_dict:
        count_dict[el] = 1
    else:
        count_dict[el] +=1

for value in count_dict.values():
    amount +=value//2

print(amount)
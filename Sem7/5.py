'''
1.Создайте список из случайных чисел. Найдите номер его последнего локального максимума (локальный максимум — это элемент, который больше любого из своих соседей).
2.Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.
3.Создайте список из случайных чисел. Найдите второй максимум.
4.Создайте список из случайных чисел. Найдите количество различных элементов в нем.
'''
# 1.
'''
import random as rnd
our_list = [rnd.randint(-5,10) for _ in range(10)]
print(our_list)
for i in range(len(our_list)-2, 0, -1):
    if our_list[i-1]<our_list[i] > our_list[i+1]:
        print(i+1, 'номер последнего локального максимума')
        break
else:
    print('локальный максимум не найдем')
'''
# 2.
# var 1
'''
import random as rnd
import time

our_list = [rnd.randint(-5,10) for _ in range(10)]
#print(our_list)

start = time.perf_counter()
max_count =0
used_set = set()
for i in our_list:
    if i not in used_set:
        count = our_list.count(i)
        if count>max_count:
            max_count = count
        used_set.add(i)

end = time.perf_counter()
a = end - start
print(max_count)


# var 2
start = time.perf_counter()
our_dict = {}

for i in our_list:
    if i not in our_dict:
        our_dict[i] = 1
    else:
        our_dict[i] +=1

max_val = max(our_dict.values())
end = time.perf_counter()
b = end - start

print(max_val)

print(a/b)
'''
# 3.
import random as rnd
import time

our_list = [rnd.randint(-5,10) for _ in range(10)]
our_list = list(set(our_list))
print(our_list)

first_max = our_list[0]
second_max = our_list[1]

if first_max < second_max:
    first_max, second_max = second_max, first_max

for i in range(2, len(our_list)):
    if our_list[i]>first_max:
        first_max, second_max =our_list[i], first_max
    elif our_list[i]>second_max:
        second_max = our_list[i]

print(second_max)
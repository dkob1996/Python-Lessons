# Есть список чисел, вводят некое число N. Нужно понять есть ли в списке такие 2 числа, что их сумма будет равна N.

# 1,2,3,4,5   #10 - нет
# 1,2,3,4,5   # 3 - есть



# Функция .count - находит кол-во повторов в списке


import random
import time

some_list = [random.randint(1, 10000) for _ in range(10 ** 6)]

start = time.perf_counter()
n = int(input())
flag = True
for i in some_list:
    if n - i in some_list:
        print(i, n - i)
        break
else:
    print('НЕТ')
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
some_set = set(some_list)
flag = True
for i in some_list:
    if n - i in some_set:
        print(i, n - i)
        break
else:
    print('НЕТ')
end = time.perf_counter()
print(end - start)
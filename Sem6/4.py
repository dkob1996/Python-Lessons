'''
Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
Программа получает на вход одно натуральное число k, не превосходящее 10^5. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. 
Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
'''
# First solving
import time
start = time.perf_counter()

def find_sum_div(num):
    summa = 0
    for div in range(1, num//2+1):
        if num % div ==0:
            summa += div
    return summa

some_dict = {}
n = int(input('Enter K: '))
for number in range(1,n+1):
    if number in some_dict:
        if find_sum_div(number) == some_dict[number]:
            print(number, some_dict[number])
    some_dict[find_sum_div(number)] = number

end = time.perf_counter()
a = end - start

# Second solving
start = time.perf_counter()

#n = int(input())
list_1 = list()
for i in range(n):
    summa = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            summa += j
    list_1.append(tuple([i, summa]))
for i in range(len(list_1)):
    for j in range(i, len(list_1)):
        if i != j and list_1[i][0] == list_1[j][1] and list_1[i][1] == list_1[j][0]:
            print(*list_1[i])

end = time.perf_counter()
b = end - start
# Third solivng - test timeing
start = time.perf_counter()

#n = int(input())
def sum_of_proper_divisors(n):
    s = 0
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            s += k
    return s

for i in range(1, 100000):
    j = sum_of_proper_divisors(i)
    if i < j <= n and i == sum_of_proper_divisors(j):
        print(i, j)

end = time.perf_counter()
c = end - start

print(a,b,c)
print('Time first method: ', a)
print('Time second method: ', b)
print('Time third method: ', c)

'''
Enter K: 100000
Time first method:  142.28573779999715
Time second method:  775.5804094999985
Time third method:  127.06894430000102
'''

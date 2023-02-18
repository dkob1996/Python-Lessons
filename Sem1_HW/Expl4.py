'''
Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
'''
n = int(input("Enter n length of chocolate: "))
m = int(input("Enter m height of chocolate: "))
k = int(input("Enter k slices of chocolate: "))

if (k < m*n) and (k % n == 0 or k % m == 0):
    print('YES')
else:
    print('NO')

'''
Complete file with 4 exercises of first python homework
'''

'''
Задача 1: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 
'''

## Solving with string and while

current_string = str(input("Enter your number: "))

lenght_of_string = len(current_string)

print(lenght_of_string)


sum =0
i = 0
while i < lenght_of_string:
    sum +=int(current_string[i])
    i +=1

print(sum)


## Solving with integer and without cycles

current_number = int(input("Enter your number: "))

result_sum = current_number%10 + current_number%100//10 + current_number%1000//100

print(result_sum)

# End of exercise one

'''
Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10
'''
'''
Math solivng
# Peter - a, Kate - b, Sergey - c
# a = x, b = y = 4*x, c = x
# all_cranes = x+4x+x = 6x
# x = all_cranes/6
'''
summary_number = int(input("Enter number of all cranes: "))
minimum_of_cranes = 6

if summary_number < minimum_of_cranes:
    print('Not anought cranes to children')
elif summary_number % 6 != 0:
    print('Number is not division by 6 without remainder')
else:
    one_crane = int(summary_number/6)
    print('Peter creates cranes: ', one_crane)
    print('Kate creates cranes: ', one_crane*4)
    print('Sergey creates cranes: ', one_crane)

# end of exercise two

'''
Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
'''
# Solving with string
ticket_number_int = int(input("Enter your ticket number: "))
ticket_number = str(ticket_number_int)
count_of_numbers_in_ticket = len(ticket_number)

sum_of_first_numbers = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
sum_of_second_numbers = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])

if count_of_numbers_in_ticket<6:
    print('Invalid count of numbers in ticket - need 6 numbers')
elif sum_of_first_numbers == sum_of_second_numbers:
    print('yes')
elif sum_of_first_numbers != sum_of_second_numbers:
    print('no')

# end of exercise 3

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

# end of exercise 4
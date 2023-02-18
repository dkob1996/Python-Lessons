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
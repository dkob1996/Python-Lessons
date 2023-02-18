'''
Task 3: Do you use public transport? You probably paid for the fare and received a ticket with a number. 
A lucky ticket is a ticket with a six-digit number, where the sum of the first three digits is equal to the sum of the last three. 
That is, the ticket with the number 385916 is a lucky one, because 3+8+5=9+1+6. You need to write a program that checks the ticket's happiness.

*Example:*

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
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
elif summary_number % 2 != 0:
    print('Number is not division by 2 without remainder')
elif summary_number % 2 == 0 and summary_number % 6 != 0:
    print('Number is not division by 6 without remainder')
elif summary_number % 2 == 0 and summary_number % 6 == 0:
    one_crane = int(summary_number/6)
    print('Peter creates cranes: ', one_crane)
    print('Kate creates cranes: ', one_crane*4)
    print('Sergey creates cranes: ', one_crane)
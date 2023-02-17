'''
Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10
'''
# Peter - a, Kate - b, Sergey - c                      7/2
# a = x, b = y = 2*x, c = x
summary_number = int(input("Enter number of all cranes: "))
minimum_of_cranes = 4
i = summary_number
if summary_number < minimum_of_cranes:
    print('Not anought cranes to children')
elif summary_number % 2 != 0:
    print('Number is not division by 2 without remainder')
elif summary_number % 2 == 0:
    while i != (i % 2 == 0):

    '''
    if summary_number % 3 == 0:
        cranes_of_x = int(summary_number/2+1)
        cranes_of_y = int(summary_number/4)
        print('Peter creates cranes: ', cranes_of_y)
        print('Kate creates cranes: ', cranes_of_x)
        print('Sergey creates cranes: ', cranes_of_y)
    else:
        cranes_of_x = int(summary_number/2)
        cranes_of_y = int(summary_number/4)
        print('Peter creates cranes: ', cranes_of_y)
        print('Kate creates cranes: ', cranes_of_x)
        print('Sergey creates cranes: ', cranes_of_y)   
'''
    '''
    cranes_of_y = int(summary_number/2)
    cranes_of_x = int(cranes_of_y/2)
    print('Peter creates cranes: ', cranes_of_x)
    print('Kate creates cranes: ', cranes_of_y)
    print('Sergey creates cranes: ', cranes_of_x)
    '''

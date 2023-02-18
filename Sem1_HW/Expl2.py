'''
Task 2: Peter, Kate and Sergey make cranes out of paper. Together they made S cranes. 
How many cranes did each child make, if it is known that Peter and Sergey made the same number of cranes,
and Kate made twice as many cranes as Peter and Sergey together?

*Example:*

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
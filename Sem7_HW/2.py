'''
### Task 36: 
Write a function print_operation_table(operation, num_rows=6, num_columns=6), 
which takes as an argument a function that calculates an element by row and column number. 
The num_rows and num_columns arguments specify the number of rows and columns of the table to be printed. 
The numbering of rows and columns starts from one (think about why not from zero). 

Note: A binary operation is any operation that has exactly two arguments, as, for example, a multiplication operation.

*Example:*

*Input:* `print_operation_table(lambda x, y: x * y) ` <br>
*Output:*
1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
'''
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        answer =[]
        for j in range(1, num_columns+1):
            answer.append(str(operation(i,j)))
        print(''.join(f'{e:<4}' for e in answer))



print_operation_table(lambda x, y: x * y)
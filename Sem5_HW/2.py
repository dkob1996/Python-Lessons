'''
Task 2
A word in this problem is a sequence of letters limited by spaces or the beginning or end of a line.
Print all the words from a row to a column. YOU CANNOT USE STRING METHODS (split)

Input format
A string is entered.

Output format
Print the words from the string one by one.

Example 1
Input

Hello, world!
Conclusion
Hello,
world!
Example 2
Input

My heart in the Highland
Conclusion
My
heart
in
the
Highland
'''
str_phrase=input('Enter your string: ')

str_one =str()
k=0

for i in range(len(str_phrase)):
    if str_phrase[i] != ' ':
        str_one +=str_phrase[i]
    if str_phrase[i] == ' ':
        k+=1
        print(str_one)
        str_one=str()

print(str_one)

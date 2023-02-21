'''
Task 1: Find the sum of the digits of a three-digit number.

*Example:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 
'''

# Solving with string and while

current_string = str(input("Enter your number: "))

lenght_of_string = len(current_string)

print(lenght_of_string)


sum =0
i = 0
while i < lenght_of_string:
    sum +=int(current_string[i])
    i +=1

print(sum)


# Solving with integer and without cycles

current_number = int(input("Enter your number: "))

result_sum = current_number%10 + current_number%100//10 + current_number%1000//100

print(result_sum)

'''
Task 30:  
Fill the array with arithmetic progression elements. 
Its first element, the difference and the number of elements must be entered from the keyboard. 
The formula for obtaining the nth term of the progression is: an = a1 + (n-1) * d.
Each number is entered from a new line.
'''
first_element = int(input('Enter first element: '))
difference = int(input('Enter difference: '))
count_of_elem = int(input('Enter count of elements: '))

list_of_el =list()
i = 0
while i<count_of_elem:
    tmp = first_element + (i)*difference
    list_of_el.append(tmp)
    i +=1
print(list_of_el)
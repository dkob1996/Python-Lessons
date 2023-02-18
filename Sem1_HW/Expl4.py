'''
Task 4: It is required to determine whether it is possible to break off k lobules from a chocolate bar with a size of n × m lobules, 
if it is allowed to make one break in a straight line between the slices (that is, break the chocolate into two rectangles).

*Example:*

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

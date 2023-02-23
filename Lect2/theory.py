# lists
list_1 = []                  # create empty list
list_2 = list()              # create empty list
list_3 = [7, 9, 11, 13, 15, 17]   # create not empty list
print(list_3[0])             # print element 0 in list 3  = 7
print(list_3)                # print all list 3

for i in list_3:             # print each element of list 3
    print(i)

print(len(list_3))           # count of elements in list 3

print(list_3[-1])            # print last element in list 3

# example wtih list
list_4 = [1, 5]
print(list_4)
list_4.append(8)             # append - add new number in the end of the list
print(list_4)

# example with list #2       # add element in list with use for i in range()
list_5 = []
for i in range(5):
    list_5.append(i)
    print(list_5)

# delete last element in list
list_6 = [12, 7, -1, 21, 0]
print(list_6.pop())          # 0            # .pop - delete last element in list
print(list_6)                # [12,7,-1,21]
print(list_6.pop())          # 21
print(list_6)                # [12,7,-1]
print(list_6.pop())          # -1
print(list_6)                # [12,7]

# delete element from list what we need
list_7 = [12, 7, -1, 21, 0]
print(list_7.pop(0))         # delete 0 element from list #12
print(list_7)                # [7, -1, 21, 0]

# add element in list in position where we need
list_8 = [12, 7, -1, 21, 0]
print(list_8.insert(2, 11))  # .insert(number of position, number what we need to add)
print(list_8)                # [12, 7, 11, -1, 21, 0]

# working with list
list_9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_9[0])                 # 1
print(list_9[1])                 # 2
print(list_9[len(list_9)-1])     # 10
print(list_9[-5])                # 6
print(list_9[:])                 # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    # [index in list where we stat : index in list where we end : step]
print(list_9[:2])                # [1,2]
print(list_9[len(list_9)-2:])    # [9,10]
print(list_9[2:9])               # [3,4,5,6,7,8,9]
print(list_9[6:-18])             # []
print(list_9[0:len(list_9):6])   # [1,7]
print(list_9[::6])               # [1,7]

# tuples
t = ()  # create empty tuple
print(type(t))  # class <'tuple'>
t = (1, )
print(type(t))  # class <'tuple'>
t = (1)
print(type(t))  # class <'int'>
t = (1,2,3)
print(type(t))

# working with tuple
v = [1,8,9]
print(v)       # [1,8,9]
print(type(v)) # class <'list'>

v = tuple(v)                      # list -> tuple
print(v)       # (1,8,9)  
print(type(v)) # class <'tuple'>

a,b = 1,2     # a = 1, b = 2
c = d = 1         # c = 1, d = 1

a1,b1,c1 = v
print (a1,b1,c1)  # a1 b1 c1

# difference beetwen list and tuple
t = (1,2,3,5,)
for i in t:       # print all tuple
    print(i)
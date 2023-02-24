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

for i in range(len(t)):   # the same
    print(t[i])

     # the most important rule - we cannot change tuple, just list #


# dictionary

dictionary = {}

dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}

print(dictionary)   # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}

print(dictionary['left'])  # ←

dictionary['left'] = '↔'
print(dictionary['left'])  # ↔

print(dictionary['type'])  # error

del dictionary['left']     # delete element

# how create dictionary
d = {}       # create empty dictionary
d = dict()   # our dictionary = dict

d['q'] = 'qwerty'  # add new element in dictionary
d['w'] = 'werty'

print(d['q'])     # print qwerty

# add new item in dictionary
dictionary[895] = 98998
print(dictionary)    # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→', 895: 98998}

# print all elements in dictionary
for item in dictionary:
    print(item)

# print all elements in special format
for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))  

# same like print all elements in special format
for (k,v) in dictionary.items():      # k - key, v - element
    print(k,v)

# view tuple in dictionary
print(dictionary.items())     # dict_items([('up', '↑'), ('left', '←'), ('down', '↓'), ('right', '→')])



# sets
colours = {'red','green','blue'}
print(colours)                 # {'green', 'red', 'blue'}

# if we add the same element in dictionary - not duplicate
colours.add('red')
print(colours)                 # {'green', 'red', 'blue'}

# add element in the end of dictionary
colours.add('gray')            # {'green', 'red', 'blue', 'gray'}
print(colours)

# get  - print without error if element banana doesn't exist
print(colours.get['banana', 'non-exist'])

# delete element from dictionary
colours.remove('red')          # {'green', 'blue', 'gray'}
print(colours)

# if we try to delete non-exist element = error
colours.remove('red')          # error
print(colours)

# if we want to avoid error, we need to use 'discard'
colours.discard('red')
print(colours)

# delete all elements in dictionary
colours.clear()  # {}
print(colours)   # set()

# if we want to create set we use:
q = set()


# operations with sets
a = {1,2,3,5,8}
b = {2,5,8,13,21}

# copy elements in a
c = a.copy()                                 # c = {1,2,3,5,8}

# join a and b
u = a.union(b)                               # u = {1,2,3,5,8,15,21}

# elements which matches in a and b
i = a.intersection(b)                        # i = {8,2,5}

# a - b
dl = a.difference(b)                         # dl = {1,3}

# b - a
dr = b.difference(a)                         # dr = {13,21}

# combination of methods
#      2          3             1
q=a.union(b).difference(a.intersection(b))   # {1,21,3,13}


# frozen sets:
a = {1,8,6}         # usually set

b = frozenset(a)    # usually set who we cannot change



# just a typical function
'''
def f(x):
    return x*x
print(f(5))
print(type(f))
'''

# calcualtor function
'''
def calc1(a,b):
    return a+b

def calc2(a,b):
    return a*b

def math(op,x,y):
    print(op(x,y))

math(calc1,5,45)
'''
# lambda - functions
'''
def calc2(a,b):
    return a*b

def math(op,x,y):
    print(op(x,y))

calc1 = lambda a,b: a+b

math(calc1,5,45)
math(lambda a,b: a+b,5,45)
'''

# exercise_1 
'''
some_list = [1,2,3,5,8,15,23,38]

def exp(a):
    some_list_1 = list()
    for i in range(len(a)):
        if a[i] %2 ==0:
            some_list_1.append((a[i],a[i]**2))
    return some_list_1

print(exp(some_list))
'''
'''
def select(f,col):
    return [f(x) for x in col]

def where(f,col):
    return [x for x in col if f(x)]

some_list = [1,2,3,5,8,15,23,38]
res = select(int,some_list)
print(res)
res = where(lambda x: x % 2 ==0, res)
print(res)
res = select(lambda x: (x,x**2), res)
print(res)
'''
# function - map 
'''
some_list =[x for x in range(1,20)]
print(some_list)

some_list = list(map(lambda x: x + 10, some_list))
print(some_list)
'''

# split + map
'''
data ='15 156 93 3 5 8 52 5'
print(data)

#data = data.split()
#print(data)

data = list(map(int, data.split()))
print(data)
'''

# exchange select to map
'''
def where(f,col):
    return [x for x in col if f(x)]

some_list = [1,2,3,5,8,15,23,38]
res = map(int,some_list)
print(res)
res = where(lambda x: x % 2 ==0, res)
print(res)
res = list(map(lambda x: (x,x**2), res))
print(res)
'''

# function filter
'''
data = [15,65,9,36,175]
res = list(filter(lambda x: x % 10 ==5, data))
print(res)
'''

# exchange where to filter
'''
some_list = [1,2,3,5,8,15,23,38]
res = map(int,some_list)
res = filter(lambda x: x % 2 ==0, res)
res = list(map(lambda x: (x,x**2), res))
print(res)
'''

# function zip
'''
users = ['user1','user2','user3','user4','user5']
ids = [4,5,9,14,7]
data = list(zip(users,ids))
print(data)                                # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]
'''
'''
users = ['user1','user2','user3','user4','user5']
ids = [4,5,9,14,7]
salary = [111,222,333]
data = list(zip(users,ids,salary))
print(data)                            # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]
'''

# function enumirate
'''
users = ['user1','user2','user3']
data = list(enumerate(users))
print(data)                        # [(0, 'user1'), (1, 'user2'), (2, 'user3')]
'''

# files
# a - open to add smth
# r - open to read smth
# w - open to record smth
# w+ - open to record and read
# r+ - open to read and record new to old info

# working with files
'''
colors = ['red', 'green', 'blue']
data = open('Lect4/file.txt', 'a', encoding='utf-8')
data.writelines(colors)
data.close()
'''
'''
with open('Lect4/file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

print(56)
'''
'''
path = 'Lect4/file.txt'
data = open(path,'r')
for line in data:
    print(line)
data.close()
'''

# OS module
'''
import os
print(os.path.basename('D:\Pyton\Lect4\funct.py'))
'''
'''
import os
print(os.path.abspath('funct.py'))
'''
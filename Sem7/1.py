'''
some_list = [1,2,3,4,5,6,7]

for ind in range(len(some_list)):
    some_list[ind] = str(some_list[ind])
print(some_list)


new_list = list(map(str, some_list))
print(new_list)

def sqare(n):
    return n**2

new_list = list(map(sqare, some_list))
print(new_list)

new_list = list(map(lambda n: n**2, some_list))
print(new_list)
'''
some_list = [1,2,3,4,5,6,7]
new_list = list(filter(lambda x: x % 2 ==0, some_list))
print(new_list)

a = [1,2,3]
b = ['1','2','3']
print(list(zip(a,b)))

number = [10,223,123,43,12]
print(list(enumerate(number)))

maxx = 0
max_el = 0
for ind,el in enumerate(number):
    if el>max_el:
        max_el = el
        maxx = ind
print(maxx)
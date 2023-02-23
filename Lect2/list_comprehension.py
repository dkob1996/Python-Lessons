## list comprehension - generator of lists

## usualy situation - list
#list_1 = [exp for item in iterable]      # list = ['something_value' for item in 'something_collection_of_date']

## use condition
#list_1 = [exp for item in iterable (if conditional)]

## create list of numbers 1 to 100
list_1 = []
for i in range(1,101):
    list_1.append(i)
print(list_1)                         # [1,2,3..,100]

# the same:
list_1 = [i for i in range(1,101)]    # [1,2,3..,100]

## create list of even numbers 1 to 100
list_1 = [i for i in range(1,101) if i%2 ==0]   # [2,4,6,..100]

# create pairs of numbers with tuples
list_1 = [(i,i) for i in range(1,101) if i%2 ==0]  # [(2,2), (4,4)...,(100,100)]

# multiply
list_1 = [i*2 for i in range(10) if i%2 ==0]   # [0,4,8,12,16]


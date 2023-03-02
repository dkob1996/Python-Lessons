'''
Task 24: 
Blueberries are grown on a farm in Karelia. 
It grows on a round bed, and the bushes are planted only around the circumference. 
Thus, each bush has exactly two neighboring ones. In total, there are N bushes growing on the bed.
These bushes have different yields, so by the time they were harvested, a different number of berries had grown on them – ai berries had grown on the i-th bush.
This farm has implemented an automatic blueberry harvesting system. This system consists of a control module and several collecting modules. 
The collecting module in one go, being directly in front of some bush, collects berries from this bush and from two neighboring ones.
Write a program to find the maximum number of berries that the collecting module can collect in one go, being in front of some bush of the garden specified in the input file.
'''


some_list = list(int((input('Enter count of berries in bush: '))) for _ in range(int(input('Enter count of bushes: '))))

some_list_count = list()
for i in range(len(some_list)):
    if i != len(some_list)-1:
        some_list_count.append(some_list[i-1] + some_list[i] + some_list[i+1])
    if i == len(some_list)-1:
        some_list_count.append(some_list[i-1] + some_list[i] + some_list[0])

print(max(some_list_count))
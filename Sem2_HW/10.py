'''
Task 10: <br>
There are n coins on the table. Some of them are tails up, and some are coats of arms. 
Determine the minimum number of coins that need to be turned over so that all the coins are turned up with the same side. 
Print the minimum number of coins to flip
'''
from random import randint
n = int(input("Enter count of coins: "))

# 0 - Heads ; 1 - Tails

count_of_heads = 0
count_of_tails = 0

for i in range(n):
    side_of_the_coin = randint(0, 1)
    # print(side_of_the_coin, end=' ')                             # testing string to see random numbers
    if side_of_the_coin == 0:
        count_of_heads +=1
    else:
        count_of_tails +=1
print()
if count_of_heads>count_of_tails:
    print('We need to return tails, this count: ', count_of_tails)
elif count_of_heads<count_of_tails:
    print('We need to return heads, this count: ', count_of_heads)
elif count_of_heads==count_of_tails:
    print('It is not important what we want to return, because count of heads and tails areh the same: ', count_of_tails)
# 5. A car travels n kilometers in a day. How many days does it take to travel a route m kilometers long?
# When solving this problem, you can not use the conditional if statement and loops.


n = int(input("Enter n kilomiters/day: "))
m = int(input("Enter m kilomiters road: "))

# first sovlving
'''
print(-(-m//n))

'''
# second sovlving
print((n + m - 1) // n)

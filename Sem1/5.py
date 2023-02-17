# 5. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.


n = int(input("Enter n kilomiters/day: "))
m = int(input("Enter m kilomiters road: "))

# first sovlving
'''
print(-(-m//n))

'''
# second sovlving
print((n + m - 1) // n)

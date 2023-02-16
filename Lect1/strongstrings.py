"""""
a = 5
b = 5.8
c = 'adada'
print(a, b, c)
print(a, ' - ', b, ' - ', c)

# F stirngs for add ' - ' easier
print(f"{a} - {b} - {c}")

print("{} - {} - {}".format(a, b, c))

# Save parameters from console
d = input()
print(d)

# Add writeline message
print('Write the 1 parameter')
d1 = input()
print(d1)

# Each method to write a -
print(a, b, c, sep= ' - ')

# Add writeline message in input function
print('Write the first number')
d1 = input()

d2 = input('Write the second number: ')

# Function of summary of parameters
print(d1, ' + ', d2, ' = ', d1 + d2) # result it's summary of strings

# Reduction of parameters

d3 = 5.89
print(d3)
print(type(d3))  # now  it's float

d3 = int(d3)
print(d3)
print(type(d3)) # now it's int

d3 = str(d3)
print(d3)
print(type(d3)) # now it's str

# now Reductuon of bool

d4 = 1
print(d4)
print(type(d4)) # now it's int

d4 = bool(d4)
print(d4)
print(type(d4)) # now it's bool and it's True

# Do summary with Reduction
print('Write the first number')
d5 = int(input())

d6 = int(input('Write the second number: '))

# Function of summary of parameters
print(d5, ' + ', d6, ' = ', d5 + d6)

# Math Operations
# +, -, *, / - classic standart
# % - the reminder of the division
# // - integer division
# ** - exponentiation

# rounding numbers
# round(parameter, count of numbers after coma) - funcion
d7 = 5.87774
d8 = 6.55557
print(round(d7*d8, 2))

# shortless assignments
iter = 2
iter += 3  # iter = iter + 3
iter -= 3  # iter = iter - 3
iter *= 3  # iter = iter * 3
iter /= 3  # iter = iter / 3
iter //= 3  # iter = iter // 3
iter %= 3  # iter = iter % 3
iter **= 3  # iter = iter ** 3

# logic operations
# >, >=, <, <=, ==, != # all like in C#
# not, and - conjuction, or- disjunction


# examples of logic operations
d9 = 1 > 4
print(d9)

d9 = 1 < 4 and 5 > 2
print(d9)

d9 = 1 == 2
print(d9)

d9 = 1 != 2
print(d9)

d9 = 'qwe'
d10 = 'qwe'
print(d9 == d10)

d9 = 1 < 3 < 5 < 10
print(d9)
"""""

# if else in python
"""""
if condition:
    # operator 1
    # operator 2
else:
    # operator n+1
    # operator n+2
"""""
# elif
"""""
if condition1:
    # operator 1
    # operator 2
elif condition2:
    # operator n+1
    # operator n+2
elif condition3:
    # operator n1+1
    # operator n1+2
else:
    # operator n2+1
    # operator n2+2

"""""
# if with and / or
"""""
if condition1 and condition2: # do when both conditions are true
    # operator 1
    # operator 2
if condition3 or condition4: # do when one of conditions is true
    # operator n+1
    # operator n+2
"""""
# example of if
"""""
username = input('Write your name: ')
if username == 'Masha':
    print('Hello, dear Masha!')
elif username == 'Dmitry':
    print('Yo, Dmitry')
elif username == 'Oleg':
    print('Good day, Oleg')
else:
    print('Hello, ', username)
"""""

# while
"""""
while condition:
    # operator 1
    # operator 2
"""""

# examples of while
n = 243
sum = 0
while n > 0:
    x = n % 10
    sum += x
    n //= 10
print(sum)  # 9

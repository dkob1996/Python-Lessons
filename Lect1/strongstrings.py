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
"""""
n = 243
sum = 0
while n > 0:
    x = n % 10
    sum += x
    n //= 10
print(sum)  # 9
"""""

# while - else
"""""
while condition:
    # operator 1
    # operator 2
else:
    # operator n+1
    # operator n+2

"""""

# example of while - else construction with break
"""""
i = 0
while i < 5:
    if i == 3:
        break       # break is not good for normal programmer, better is a flag parameter
    i += 1
else:
    print('Let us')
    print('stop')
print(i)
"""""

# example while elif with flag
"""""
n = int(input())
flag = True
i = 2
while flag:
    if n % i ==0: # if reminder n/i == 0
        flag = False
        print(i)
    elif i>n //2: # i need to be smaller then n / 2
        print(n)
        flag = False
    i += 1
"""""

# for
"""""
for i in enumeration:
    # operator 1
    # operator 2
    ...
"""""

# example of for
"""""
for i in 1, -2, 3, 14, 5:
    print(i)
"""""

# range() function which generate sequence
"""""
# range(start number, end number, step(default = 1))

r = range(5) # 0 1 2 3 4 
r = range(2,5) # 2 3 4
r = range(0,-5) # ----
r = range(1,10,2) # 1 3 5 7 9  
r = range(100, 0, -20) # 100 80 60 40 20

for i in r:
    print(i)
    # 100 80 60 40 20
"""""

# for with range()
"""""
for i in 'qwerty':
    print(i)

# q
# w
# e
# r
# t
# y

"""""

# example for with range()

a = 'qwery'
"""""
print(a[0])
"""""
"""""
for i in a:
    print(i)
"""""
"""""
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)
"""""

# strings
"""""
text = 'eat more THIS softly FRANCHE cakes'
print(len(text))                             # length of string
print('more' in text)                        # true or false word in string
print(text.lower())                          # all words in string small
print(text.upper())                          # all words in string capital
print(text.replace('more', 'MORE'))          # edit string (more (before) -> More (now))
"""""

# working with string
text = 'eat more THIS softly FRANCHE cakes'
# print(text[start number letter, end number letter, step])
print(text[0])                               # e
print(text[1])                               # a
print(text[len(text)-1])                     # s
print(text[-5])                              # c
print(text[:])                               # eat more THIS softly FRANCHE cakes
print(text[:2])                              # ea
print(text[len(text)-2:])                    # es
print(text[2:9])                             # t more
print(text[6:-18])                           # re THIS so
print(text[0:len(text):6])                   # erSlNa
print(text[::2])                             # etmr HSsfl RNH ae

print(text[-1])                              # count goes of the end of the string # s

text = text[2:9] + text[-5] + text[:2]
print(text)                                  # t more cea
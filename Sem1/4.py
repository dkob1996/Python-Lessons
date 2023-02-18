# 4. The user enters an integer. Print YES if this number has four digits and NO otherwise.


# without circles
"""""
number = int(input("Enter number: "))
if number > 999 and number < 10000:
    print("YES")
else:
    print("NO")
"""""

# with circle
"""""
number = int(input("Enter number: "))

count =0

while number >0:
    number //=10
    count +=1

if count ==4:
    print("YES")
else:
    print("NO")
"""""
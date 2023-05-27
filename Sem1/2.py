# 2. Two integers are given: A, B. Check the truth of the statement: "The numbers A and B have the same parity"

first_number = int(input("Enter A number: "))
second_number = int(input("Enter B number: "))

if first_number % 2 == 0 and second_number % 2 == 0:
    print("A and B paritys are similar")
else:
    print("A and B paritys are not similar")
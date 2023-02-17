# 2. Даны два целых числа: A, B. Проверить истинность высказывания: "Числа A и B имеют одинаковую четность"

first_number = int(input("Enter A number: "))
second_number = int(input("Enter B number: "))

if first_number % 2 ==0 and second_number % 2 ==0:
    print("A and B paritys are similar")
else:
    print("A and B paritys are not similar")
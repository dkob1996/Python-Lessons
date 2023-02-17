# 6. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

number_of_children_in_first_class = int(
    input("Enter count of childrens in first classroom"))
number_of_children_in_second_class = int(
    input("Enter count of childrens in second classroom"))
number_of_children_in_third_class = int(
    input("Enter count of childrens in third classroom"))

cound_desk_first_class = number_of_children_in_first_class//2 + \
    number_of_children_in_first_class % 2

cound_desk_second_class = number_of_children_in_second_class//2 + \
    number_of_children_in_second_class % 2

cound_desk_third_class = number_of_children_in_third_class//2 + \
    number_of_children_in_third_class % 2

print(cound_desk_first_class+cound_desk_second_class+cound_desk_third_class)

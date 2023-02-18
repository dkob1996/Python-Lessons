# 6. At some school, they decided to recruit three new math classes and equip classrooms for them with new desks.
# Two students can sit at each desk. 
# The number of students in each of the three classes is known.
# Output the least number of desks to be purchased for them.

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

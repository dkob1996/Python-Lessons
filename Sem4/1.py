# 25.
# Напишите программу, которая принимает на вход строку, и отслеживает кол-во повторов каждого символа.
# Пример:
# Бессмертный
# б -1, е - 2, с - 2, м - 1

import time
import random

some_str = [chr(random.randint(0, 100)) for _ in range(1000000)]

start = time.perf_counter()
used_set = set()
for letter in some_str:
    if letter not in used_set:
        a = f'{letter} - {some_str.count(letter)}'
        pass
    used_set.add(letter)
end = time.perf_counter()
first_time = end - start

start = time.perf_counter()
letter_count_dict = {}
for letter in some_str:
    if letter not in letter_count_dict:
        letter_count_dict[letter] = 1
    else:
        letter_count_dict[letter] += 1
# print(letter_count_dict)
end = time.perf_counter()
second_time = end - start
print(first_time / second_time)
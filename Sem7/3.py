'''
Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет 
самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет 
ту, по которой вращается самая далекая планета. 
Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких 
планет нет, зато искусственные спутники были запущены на круговые орбиты. Результатом функции должен быть кортеж,
содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары 
чисел - полуосей ее эллипса. 

Площадь эллипса вычисляется по формуле S = piab, где a и b - длины полуосей эллипса. 
При решении задачи используйте списочные выражения. 

Подсказка: проще всего будет найти эллипс в два шага: сначала 
вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая 
далекая планета ровно одна

Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
Вывод:
2.5 10
'''
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

'''
def find_farthest_orbit(list_of_orbits):
    maxx = list_of_orbits[0]
    for el in list_of_orbits:
        if el[0] != el[1]:
            if el[0] * el[1] > maxx[0] * maxx[1]:
                maxx = el
    return maxx
print(*find_farthest_orbit(orbits))
'''


def find_farthest_orbit(list_of_orbits):
    list_of_orbits = list(filter(lambda el: el[0] != el[1], list_of_orbits))
    maxx = max(list(map(lambda el: el[0] * el[1], list_of_orbits)))
#    maxx = max([el[0]* el[1] for el in list_of_orbits])
    maxx_tuple = filter(lambda x: x[0]*x[1] == maxx, list_of_orbits)
    return maxx_tuple


print(*find_farthest_orbit(orbits))

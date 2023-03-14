with open('Sem8/4_info3.txt', 'w', encoding='utf-8') as res:
    with open('Sem8/4_info1.txt', 'r', encoding='utf-8') as file:
        line_1 = file.readline()
        while line_1:
            res.write(line_1)
            line_1 = file.readline()
        res.write('\n')
    with open('Sem8/4_info2.txt', 'r', encoding='utf-8') as file:
        line_1 = file.readline()
        while line_1:
            res.write(line_1)
            line_1 = file.readline()


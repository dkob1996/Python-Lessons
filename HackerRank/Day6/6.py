str_1 =[input('Enter strings: ') for _ in range(int(input('Enter count of strings: ')))]
#str_1 = ['Hacker','Rank']


str_2= [str()]
str_3 =[str()]

for i in str_1:
    str_tmp = str()
    str_tmp1 = str()
    for j in range(0,len(i),2):
        str_tmp +=i[j]
    str_2.append(str_tmp)


    for k in range(1,len(i),2):
        str_tmp1 +=i[k]
    str_3.append(str_tmp1)


print(str_2[1]+ ' ' +str_3[1])
print(str_2[2]+ ' ' +str_3[2])
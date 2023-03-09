T = int(input('Enter count of strings: '))

for i in range(0, T):
    S = input('Enter string: ')
    print(S[0::2]+ ' '+S[1::2])
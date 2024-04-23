str1 = ''
for i in range(0,9):
    if i < 5:
        str1 += '* '
        print(str1)
    elif i > 4:
        str1 = str1[:-2]
        print(str1)

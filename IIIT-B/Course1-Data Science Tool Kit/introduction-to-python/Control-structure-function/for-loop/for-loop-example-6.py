'''
Total number of pairs 36

find probablity of number  


'''
number = 0

for i in range(1,7):
    for j in range(1,7):
        if(i + j ==8):
            number = number +1
            print(i,j)
print(number)
print(round((number/36)*100,2))
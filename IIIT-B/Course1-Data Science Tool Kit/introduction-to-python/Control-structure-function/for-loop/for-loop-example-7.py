'''
if we are rolling two dice what will be probablity of getting total  


'''
for n in range(1,13):
    number = 0
    for i in range(1,7):
        for j in range(1,7):
            if(i + j ==n):
                number = number +1
    print(n, '=',round((number/36)*100,2),'%')
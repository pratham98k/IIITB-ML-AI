'''
nested for loop

if we are rolling three dice what will be probablity of getting total in percent

'''
for n in range(1,19):
    number = 0
    for i in range(1,7):
        for j in range(1,7):
            for k in range(1,7):
                if(i + j + k ==n):
                    number = number +1
        print(n, '=',round((number/216)*100,2),'%')
#find the number is divisible by 5 and 3
n = int(input("Enter the number: " ))

if (n % 5 == 0):
    if (n % 3 == 0):
        print("it's divisible by 5 and 3" )
    else:
        print('not divisible') # this will execute if number is not divisible by 3
else:
    print('not divisible') # this will execute if number is not divisible by 5
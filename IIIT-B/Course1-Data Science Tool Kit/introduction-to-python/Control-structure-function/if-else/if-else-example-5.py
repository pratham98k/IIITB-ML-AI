'''
n = 15

      (n % 5 == 0 ) and (n % 3 == 0)

n=15     true and true   = true

n=20      true and false = false

n=12      false and true  = false

11         false and false = false

this program reduce number of lines as compare to if else example 4

we can keep adding and multiple condition 

if ((n%5 == 0) and (n%3 ==0)) and (n%7 ==0):

'''

n = int(input("Enter the number: " ))

if ((n%5 == 0) and (n%3 ==0)):
    print('Divisible')
else:
    print('not divisible')
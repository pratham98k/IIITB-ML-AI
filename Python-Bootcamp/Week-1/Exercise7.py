'''
Sum of digits
Description
Write a program to calculate the sum of the digits of a given number 

----------------------------------------------------------------------
Input:
An n digit number

Output:
Sum of the digits

----------------------------------------------------------------------
Sample input:
983

Sample output:
20

----------------------------------------------------------------------
Sample input:
5241

Sample output:
12

=======================================================================
#Take input
n=int(input())

#Creating a variable sum that will store the sum of the digits
sum=0

while (n>0):
    # n%10 gives the reminder value(=digit)
    sum=sum+n%10
    
    # Updating the value of n by dividing it by 10 inorder to get the next digit during next iteration
    n=n//10

#Print the result
print(sum)



'''

n=int(input())

# write your code here
total=sum(map(int,str(n)))

# print the results
print(total)


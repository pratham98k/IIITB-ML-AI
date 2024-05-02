'''
Valid triangle
Description
Write a program to accept three sides of a triangle as the input and print whether the triangle is valid or not.
(A triangle is valid if the sum of any two sides is greater than the third side.)



----------------------------------------------------------------------
Input:
Three sides of a triangle separated by a space

Output:
Whether the given triangle is "Valid" or "Invalid"

----------------------------------------------------------------------
Sample input:
3 4 5

Sample output:
Valid

----------------------------------------------------------------------
Sample input:
1 4 5

Sample output:
Invalid

=======================================================================
#Take inputs
a,b,c=input().split()

#Convert string to float type
a=float(a)
b=float(b)
c=float(c)

#check if the all possible sum of two sides is greater than the third side

if b+c>a and a+c>b and a+b>c:
    print("Valid")

else:
    print("Invalid")
    

'''

# Take input
a,b,c= input().split()

# Write your code here
# Convert a,b,c into numeric type and check for the validity of triangle
a =int(a)
b =int(b)
c =int(c)
if (a+b<=c) or (b+c<=a) or (a+c<=b):
    print("Invalid")
else:
    print("Valid")

#print result



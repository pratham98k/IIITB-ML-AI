'''
ASCII values
Description
Write a program to accept a character and display its next and previous character. 

Hint: Make use of Ascii values here.

----------------------------------------------------------------------
Input:
A character

Output:
Previous character and the next character of the given character

----------------------------------------------------------------------
Sample input:
D

Sample output:
C
E

----------------------------------------------------------------------
Sample input:
8

Sample output:
7
9

----------------------------------------------------------------------
Sample input:
@

Sample Output: 
?
A
=======================================================================
# Take input
x=input()
#Write your code here
print(chr(ord(x)-1))
print(chr(ord(x)+1))



'''

# Take input
x=input()
#Write your code here
print(chr(ord(x)-1))
print(chr(ord(x)+1))
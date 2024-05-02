'''
Character frequency
Description
Write a program to accept a string value from the user and accept a char value from the user and find out the total occurrence of the char value in the string value. Note that the count is not case-sensitive

----------------------------------------------------------------------
Input:
A string and a character whose occurrence is to be found

Output:
An integer

----------------------------------------------------------------------
Sample input:
Python Programming
P

Sample output:
2

----------------------------------------------------------------------
Sample input:
This is my first program
t
Sample output:
2
======================================================================
upgrad

# Take input
input_string=input()
input_char=input()

#Check the count of input_char in the string input_string and print it
input_char=input_char.lower()
print(input_string.lower().count(input_char))


'''

input_string=input()
input_char=input()

#write your code here
lc= input_char.lower()
hc= input_char.upper()

fc= input_string.count(lc) + input_string.count(hc)
print(fc)
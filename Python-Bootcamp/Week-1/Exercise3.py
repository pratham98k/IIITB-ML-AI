'''
No Vowels
Description
Write a program to accept a string from the user, delete all vowels from the string and display the result. 

----------------------------------------------------------------------
Input:
A string

Output:
A string with vowels removed

----------------------------------------------------------------------
Sample input:
Upgrad

Sample output:
pgrd


----------------------------------------------------------------------
Sample input:
Python Programming

Sample output:
Pythn Prgrmmng
======================================================================
# Take input
s=input()

# Write your code here
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for char in s:
    if char not in vowels:
        result = result + char
print(result)


'''

# Take input
s=input()

#Creating an empty string that will store the modified string
s_new=''

#Looping the string 's' and extracting only the consonants
for i in range(len(s)):
    if s[i] not in "AEIOUaeiou":
        s_new=s_new+s[i]

#Print the result

print(s_new)
'''
Length of list elements
Description
Given a list of strings, write a program to find the number of strings whose length is greater than or equal to K, where K is a positive integer.

Input - List of strings and an integer
﻿Output - Integer

--------------------------------------------------------------------------------

Sample Input :
[Mumbai, Hyderabad, Calicut, Chennai]
  9

Sample Output: 1

-------------------------------------------------------------------------------

Sample Input :
[Datascience, Data Analyst, Programmer, Manager]
  8

Sample Output : 3


'''

input_list_str = input()
input_list = input_list_str.strip("[]").split(", ")
K = int(input())

print(input_list[0])
print(len(input_list[0]))
for i in input_list:
    print(len(i))


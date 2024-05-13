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
import ast

#Take input
input_list = ast.literal_eval(input())
K= int(input())

# Initialising a count variagble that tracks the number of elements in the list
# with length >k
count = 0

#Looping through the list and check the length of each element. Increase the count by 1 if the 
#length is greater than K
for i in input_list:
	if len(i)>=K:
	    count=count+1
	    
print(count)




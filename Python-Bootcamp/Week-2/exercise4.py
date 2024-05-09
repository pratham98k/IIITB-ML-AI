'''
Slicing a list
Description
Given a list of strings and an integer K, write a python code to print all the elements from the K th position till the end of the list.

Note: Assume that K (a positive integer) will always be less than or equal to the length of the list
Input - A list of strings in the first line and an integer in the second line of the input.
Output - A list

--------------------------------------------------------------------------------------------------------

Sample Input :
['Mumbai', 'Delhi', 'Australia', 'Nigeria', 'USA', 'London', 'Canada']
2

Sample Output : ['Delhi', 'Australia', 'Nigeria', 'USA', 'London', 'Canada']

--------------------------------------------------------------------------------------------------------
Sample Input :
['Chennai', 'Vizag', 'Austria', 'Germany', 'Japan']
3

Sample Output : ['Austria', 'Germany', 'Japan']

'''
#taking the input from user
import ast
input_lst = input()
test_lst = ast.literal_eval(input_lst)
K= input()
K= int(K)

print(test_lst[K-1:len(test_lst)])

'''
Increment list elements
Description
Given a list of strings, increment the value of the numeric strings by 'k’. 

Hint: The function isdigit() may be useful here.

---------------------------------------------------------------------------------------------

Input - A list in the first line and an integer in the second line
Output - A list
---------------------------------------------------------------------------------------------
Sample Input :
['Python', '123', 'Data']
  4
Sample Output : ['Python', '127', 'Data']

--------------------------------------------------------------------------------------------
Sample Input :
['upGrad', '1991', 'Mumbai']
  0

Sample Output : ['upGrad', '1991', 'Mumbai']

---------------------------------------------------------------------------------------------
Sample Input :
['Data Science', '100', '10']
  10

Sample Output : ['Data Science', '110', '20']


'''

import ast
#reading the input list
input_list = ast.literal_eval(input())
K = int(input())

# Function that takes the input list and increment value as an argument 
def check(L, K):
    for i in range(len(L)):
        # incrementing on testing for digit, increment by K or else continue the loop 
        if L[i].isdigit(): 
            L[i] = str(int(L[i])+K)
        else: 
            continue
    return L


#calling the function
transformed_list = check(input_list, K)

#print the result
print(transformed_list)

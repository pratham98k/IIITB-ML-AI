'''
Merge dictionaries
Description
Write a python code to merge two dictionaries into a single dictionary.

--------------------------------------------------------------------------------------------------

Input: Two dictionaries, one in each line

Output: A Dictionary

--------------------------------------------------------------------------------------------------

Sample Input :
{'a': 10, 'b': 8}
{'d': 6, 'c': 4}

Sample Output : {'c': 4, 'a': 10, 'b': 8, 'd': 6}

--------------------------------------------------------------------------------------------------

Sample Input :
{'a': 110, 'b': 88}
{'d': 62, 'c': 44}

Sample Output : {'a': 110, 'b': 88, 'd': 62, 'c': 44}

--------------------------------------------------------------------------------------------------
import ast

#taking the input from user
input_dict1 = input()
dict1= ast.literal_eval(input_dict1)
input_dict2 = input()
dict2= ast.literal_eval(input_dict2)

#updating dict1 with dict2
dict1.update(dict2)
print(dict1)



'''
#mysolution
import ast
#reading the input dictionary
input_dictionary1 = input()
convert_dictionary1 = ast.literal_eval(input_dictionary1)

input_dictionary2 = input()
convert_dictionary2 = ast.literal_eval(input_dictionary2)

dict3=convert_dictionary1.copy()
dict3.update(convert_dictionary2)
print(dict3)
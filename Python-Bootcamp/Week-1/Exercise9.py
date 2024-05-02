'''
String manipulation
Description
Write a program that takes a string as the input and does the following:
    -Removes the numbers, special characters
    -Converts uppercase letters to lowercase letters, and vice versa 
    
----------------------------------------------------------------------
Input:
A string 

Output:
A string with numbers, special characters removed, upper and lower cases swapped

----------------------------------------------------------------------
Sample input:
Programming1234

Sample output:
pROGRAMMING


----------------------------------------------------------------------
 Sample input:
 Programming is 100% fun
Sample output:
pROGRAMMINGISFUN


'''

#Take input
input_string=input()

#Initialising an empty string that will store the modified resultant string
new_str=''

# looping through the input_string where 'c' is each character of the string
for c in input_string:

    # if the character 'c' is an alphabet, implement the code following otherwise skip that character and go for next iteration
    if (c.isalpha()):
        
        # if the character 'c' is an uppercase, convert it into lowercase otherwise convert the character into uppercase
        if c.isupper():
            new_str=new_str+c.lower()
        else:
            new_str=new_str+c.upper()
        

print(new_str)

'''
Updating the dictionary keys
Description
You are provided with a dictionary containing the names of different football clubs as keys and the name of the main player of the corresponding team as values. When the main player of a team retires, one of their teammates steps up to fill in their role as the main player.
You’re also provided with a list which contains the names of the football clubs for which the current main players are retiring and the names of the corresponding new main player. Your task is to update the values in the original dictionary with the names of the new main players.

------------------------------------------------------------------------------------------------------

Input - The input consists of a dictionary with different football clubs' names and their main player. In the next line, you will be provided with a list of the new players who have taken up the main roles.

Output - Dictionary
---------------------------------------------------------------------------------------------------

Sample Input :
{Barcelona:’Messi’ , ‘Real Madrid’: ‘Benzema’, ‘PSG’: ‘Neymar’ }
[[‘Barcelona’, ‘Griezmann’], [‘PSG’, ‘Ramos’]]

Sample Output: {Barcelona:‘Griezmann’, ‘Real Madrid’: ‘Benzema’, ‘PSG’: ‘Ramos’}

---------------------------------------------------------------------------------------------------

Sample Input:
{Liverpool:’A’, ‘Real Madrid’: ‘B’, ‘Chelsea’: ‘C’ }
[[Liverpool, ‘R’]]

Sample Output: {Liverpool:’R’, ‘Real Madrid’: ‘B’, ‘Chelsea’: ‘C’ }


---------------------------------------------------------------------------------------------------

Sample Input :
 {Atletico Madrid : ’D’ , ‘Juventus’: ‘B’, ‘Chelsea’: ‘C’ }
[[‘Juventus’, ‘G’], [‘Chelsea’, ‘H’]]

Sample Output: {Atletico Madrid : ’D’, ‘Juventus’: ‘G’, ‘Chelsea’: ‘H’ }
=====================================================================================
import ast
#reading the input dictionary
input_dict = ast.literal_eval(input())

#reading the input list
input_list = ast.literal_eval(input())

#Function to update the keys of the dictionary
def check(d,l):
    #loop through each key-value pair in the dictionary
    for key in d.keys():
        # loop through the list
        for ele in l:
            #check if any element of the sub list matches the key
            if ele[0]==key:
                #update the value
                d[key] = ele[1] 
            else: 
                pass
    return d

#calling the function
transformed_dictionary = check(input_dict, input_list)
#print the result
print(transformed_dictionary)




'''
#MY solution
#Take input here
#we will take input using ast sys
import ast
#reading the input dictionary
input_dictionary = input()
convert_dictionary = ast.literal_eval(input_dictionary)

#reading the input list
input_list = input()
convert_list = ast.literal_eval(input_list)

#Write code here
list3=[]
for i in convert_list:
    list3.append(tuple(i))
d=dict(list3)
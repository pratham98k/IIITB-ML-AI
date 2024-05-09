'''
List average
Description
Suppose you are working as a Marketing Lead in a company and you want to recruit new employees in your team (which already consists of 10 members) to carry out the company’s major project. You select the employees based on five parameters: A, B, C, D and E. The value of each parameter is represented on a scale of 1 to 10. The present average value of these parameters for your team is given to you in a list (in the same order). You recruit a person only if their scores do not reduce the average score of more than two parameters of your team. If they are recruited, print the output as ‘Selected’. If not, print the output as ‘Rejected’.

--------------------------------------------------------------------------------------------------

Input - Two lists, where the first list is the average scores of the team in the five parameters, and the second list is the scores of the new employee in all the five parameters. The parameter order is the same for both the lists, which is A, B, C, D and E.

Output - String

--------------------------------------------------------------------------------------------------

Sample Input - [‘8’, ‘4’, ‘6’, ‘9’, ‘7’]
  [‘1’, ‘1.1’, ‘1.2’, ‘1.2’, ‘2.3’]

Sample Output - Rejected

--------------------------------------------------------------------------------------------------

Sample Input - [‘10’, ‘5’, ‘6’, ‘9’, ‘7’]
  [‘10’, ‘ 9.8’, ‘7.2’, ‘1.66’, ‘4.3’]

  Sample Output - Selected

--------------------------------------------------------------------------------------------------

Sample Input - [‘8’, ‘5.66’, ‘6.5’, ‘10’, ‘10’]
  [‘7’, ‘ 10’, ‘6’, ‘7’, ‘9’]

Sample Output - Rejected
=========================================================================================================
#upgrade solution 


import ast
#taking the input from user which is the scores of the team
input_list = input()
team_list = ast.literal_eval(input_list)

#taking the input from user which is the scores of the new employee
input_list = input()
new_member_list = ast.literal_eval(input_list)

def check(team_list, new_member_list):
    total = 0
    #loop through every element of the list
    for i in range (0, len(team_list)):
        #calculate the average score after adding the new member score
        #the 10 denotes the number of employees already existing
        # after adding the new employee it becomes 11
        average = (float(team_list[i])*10+float(new_member_list[i]))/11
        #check if average is improved or not
        if average>=float(team_list[i]):
            #keep a count on the number of parameters
            total+=1
            
    if total>=3:       
        return "Selected"    
    else:
        return "Rejected"
#calling the function
validity = check(team_list, new_member_list)
#print the result
print(validity)



'''
#my solution
import ast
#reading the input dictionary
#reading the input list
input_list1 = input()
convert_list1 = ast.literal_eval(input_list1)
#Write the code here
input_list2 = input()
convert_list2 = ast.literal_eval(input_list2)

def compare_lists(list1, list2):
    for elem1, elem2 in zip(list1, list2):
        if float(elem1) < float(elem2):
            return "Selected"
    return "Rejected"

print(compare_lists(convert_list1, convert_list2))

'''
List sum

Suppose you want to know the total score of the Indian cricket team in a given match. To do so, your task is to find the sum of all the scores of the Indian team players. The scores are provided as a list, with each element as an individual score of the players. Also, there is a condition that if the number of elements in the list is more than 11, then it is an invalid input and the output should be -1.

--------------------------------------------------------------------------------------------

Input - List
Output - An integer

--------------------------------------------------------------------------------------------

Sample Input : [11, 13, 101, 14, 33, 141]
Sample Output : 313

---------------------------------------------------------------------------------------------

Sample Input : [11, 13, 101, 14, 33, 141, 12, 144, 54, 67, 8, 11]
Sample Output : -1
---------------------------------------------------------------------------------------------

Sample Input : [100, 80, 30, 10, 0, 1, 2, 0]
Sample Output : 223

---------------------------------------------------------------------------------------------


'''
import ast

#Take scores list as input
scores=ast.literal_eval(input())

#Function for calculating the total scores that takes the scores list as an argument

def calc_score(scores):

#If the number of score entries in the list is greater than 11, return -1
    if len(scores)>11:
        return(-1)
        
#calculate the sum of scores
    else:
        return(sum(scores))

print(calc_score(scores))

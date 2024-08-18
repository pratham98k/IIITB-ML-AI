List []

Tupile () Tupil once created can not be changed


Dictorary {} 


How we insert multiple elements at the same time at the end of a list ?
Given Input :

a = [1, 2, 3, 4, 5]

b = [6, 7, 8, 9]

 

Insert the elements of list b at the end list a . So final output

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

 

python code :

a.extend(b)

 

Note :

If you use a.append(b) then it will give wrong output ([1, 2, 3, 4, 5, [6, 7, 8, 9]]) so basically it is appending whole list at the end of original list.
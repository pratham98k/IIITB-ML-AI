'''
Substring with maximum uppercase characters
Description
Given a string, write a Python program to find the largest substring of uppercase characters and print the length of that substring. Check the sample inputs and outputs for a better understanding.

---------------------------------------------------------------------------------------------------
Input - String
Output - String
---------------------------------------------------------------------------------------------------

Sample Input - I lovE PRogrAMMING

Sample Output - 6

Explanation - AMMING is the largest substring with all characters in uppercase continuously 

-----------------------------------------------------------------------------------------------------
Sample Input - MuMbaI is in MAHArashTRA
Sample Output - 4

Explanation - MAHA is the largest substring with all characters in uppercase continuously.

---------------------------------------------------------------------------------------------------
Sample Input - India WOn the WOrLD CUP
Sample Output - 3

Explanation - CUP is the largest substring with all characters in uppercase continuously.

example version 

https://www.tutorialspoint.com/python-program-to-find-maximum-uppercase-run#:~:text=The%20input%20string%20is%20searched,findall()%20function.



'''

#read the string
test_str = input()

# when a character in the string is a uppercase, cnt will count the number of #continuous uppercase characters from that index
cnt=0
# max_run stores the final maximum count which is to be displayed as answer
max_run=0

for i in range(0,len(test_str)):
    # updating run count on uppercase 
    if test_str[i].isupper():
        cnt=cnt+1
    # on encountering lowercase, update the cnt with 0 and start counting the continuous uppercase run again. max_run  already has the count of this run stored.
    #updating the value of max_run with cnt, if the current ‘cnt’ is greater than the previous ‘max_run’
    else:
        if cnt>=max_run:
            max_run=cnt
        cnt=0
#for boundary cases - when there is a potential longest substring at the end of the string        
if cnt>=max_run:
    max_run=cnt
    
# printing result 
print(max_run)

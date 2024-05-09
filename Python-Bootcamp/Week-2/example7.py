'''
Divisibility check
Description
Given an integer ‘n’, your task is to write a Python code to find whether ‘n’ is divisible by all its digits or not. If they divide the number, then the number ‘n’ is a happy number. Otherwise, it is a sad number.
The number ‘n’ may be provided with commas. At first, you have to clean the number (by removing the commas involved) and then check whether the number is happy or sad.
---------------------------------------------------------------------------------------------------

Input - String
Output - String

---------------------------------------------------------------------------------------------------
Sample Input - 2,128
Sample Output - Happy Number

---------------------------------------------------------------------------------------------------
Sample Input - 256
Sample Output - Sad Number

---------------------------------------------------------------------------------------------------

Sample Input - 1124
Sample Output - Happy Number

---------------------------------------------------------------------------------------------------
====================================================================================================
# reading input
test_str = input()

#replace special characters in number, here it is comma (,)
cleaned_test_str = test_str.replace(",","")

#convert to integer
n = int(cleaned_test_str)

# Function to check if all digits of n divide it or not
def allDigitsDivide(n):
    temp = n
    while (temp > 0):
        # Taking the digit of the number into a digit variable.
        digit = temp % 10

         #check if the digit is non-zero as any number dividing zero is invalid
         #also check if it gives a remainder of zero when it divides n
        if not(digit != 0 and n % digit == 0):
	        return False
        temp = temp // 10
    
    #If the function did not return anything until the while loop is over, 
    #it means that the number was divisible by all of its digits.
    return True
    
#call the allDigitsDivide function
if (allDigitsDivide(n)):
    print("Happy Number")
else:
    print("Sad Number" )


'''
#my answer
n=input()
n = n.replace(',', '')
    
    # Convert the cleaned number to an integer
num = int(n)
    
    # Iterate through each digit of the number
for digit in n:
    if int(digit) != 0:
        if num % int(digit) != 0:
            print("Sad Number")
            break
    print("Happy Number")
    break
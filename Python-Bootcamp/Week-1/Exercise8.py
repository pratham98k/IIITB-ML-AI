'''
Count the digits
Description
Write a program to accept a number from the user and count the zeros, odd digits and non-zero even digits from the entered number.

----------------------------------------------------------------------
Input:
A positive integer of n digits

Output:
Three integers representing the occurrences of zeros, odd digits and non-zero even digits from the entered number.
----------------------------------------------------------------------
Sample input:
1030

Sample output:
Number of odd digits: 2
Number of non-zero even digits: 0
Number of zeros: 2

=========================================================================
upgrade

# Take input
n=int(input())

# creating three variables to keep the count of odd, even and zero digits
n_odd=0
n_even=0
n_zeros=0



while n>0:

# Storing the reminder(is also digit at one's place of n) of n%10
    r=n%10

    # If the reminder(is also digit at one's place of n) is 0, the digit is 0. Increase the count of zeros by 1
    if r==0:
        n_zeros+=1
        
    #If the reminder is divisible by 2, it is an even digit otherwise odd. Increase the respective counts
    elif r%2==0:
        n_even+=1
        
    else:
        r%2==1
        n_odd+=1
    
    # Updating the value of n by dividing it by 10 inorder to get the next digit during next iteration
    n=n//10
        
#Print the results
print("Number of odd digits:",n_odd)
print("Number of non-zero even digits:",n_even)
print("Number of zeros:",n_zeros)

'''
# Take input
n=int(input())
# Input from the user


# Convert number to string
num_str = str(n)

# Initialize counters
zero_count = 0
odd_count = 0
even_count = 0

# Iterate through each digit
for digit in num_str:
    if digit == '0':
        zero_count += 1
    elif int(digit) % 2 == 0 and digit != '0':
        even_count += 1
    else:
        odd_count += 1

# Output
print("Number of odd digits:", odd_count)
print("Number of non-zero even digits:", even_count)
print("Number of zeros:", zero_count)

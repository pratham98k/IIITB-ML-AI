'''
If-Else
Description
Write a code to check if the string in input_str starts with a vowel or not. Print capital YES or NO.

For example, if input_str = 'analytics' then, your output should print 'YES'.

Sample Input:
alpha

Sample Output:
YES
======================================================================================================
import ast,sys
input_str = sys.stdin.read()

if input_str[0] in ['a','e','i','o','u','A','E','I','O','U']:
    print('YES')
else:
    print('NO')



'''

import ast,sys
input_str = sys.stdin.read()

x = input_str[0]

x= x.lower()


if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
    print("YES")
else:
    print("NO")
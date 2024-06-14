## Case 1
# This function basically takes two number as a input from the user
# Then performs the division and squares the result

def get_squared_list(times):
    count, num_1, num_2, sqrd_list = 0, 0, 0, []

    while count < times:
        print('----------------Iteration {}----------------'.format(count + 1))
        # Beginning of a try block
        try:
            num_1 = int(input('Enter the first number : '))
            num_2 = int(input('Enter the second number : '))
            sqrd_list.append((num_1 // num_2) ** 2)

        # In case num_2 == 0 this error will be raised
        except ZeroDivisionError as z_e:
            print('__! Divisor cannot be zero !__')
            print('Error : {}'.format(z_e))

        # If input is invalid this error will be raised
        except ValueError as v_e:
            print('__! Invalid Input !__')
            print('Input must be an integer')
            print('Error : {}'.format(v_e))

        # All the other unknown errors can be handled by this exception handler
        except Exception as e:
            print('General exception handler')
            print('Error : {}'.format(e))

        else:
            print('Code Executed Successfully')
            print('No Exceptions occured')

        count += 1
        print('\n')


if __name__ == '__main__':
    count = int(input('Enter the count :'))
    get_squared_list(count) # Case 1 Execution starts
 




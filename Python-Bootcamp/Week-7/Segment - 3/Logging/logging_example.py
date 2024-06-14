import logging

## It's not ideal in production environment to just handle the exception and
## leave other details like when exception occured or what was the problem
## To handle such issues you need exception handling


## Case 1
# This function basically takes two number as a input from the user
# Then performs the division and squares the result

def get_squared_list(times):
    count, num_1, num_2, sqrd_list = 0, 0, 0, []

    while count < times:
        print('-------------Iteration {}---------------'.format(count + 1))

        # Beginning of a try block
        try:
            num_1 = int(input('Enter the first number : '))
            num_2 = int(input('Enter the second number : '))
            sqrd_list.append((num_1 // num_2) ** 2)

        # In case num_2 == 0 this error will be raised
        except ZeroDivisionError as z_e:
            print('__! Divisor cannot be zero !__')
            # print('Error : {}'.format(z_e))
            logger.error(z_e)

        # If input is invalid this error will be raised
        except ValueError as v_e:
            print('__! Invalid Input !__')
            print('Input must be an integer')
            # print('Error : {}'.format(v_e))
            logger.error(v_e)

        # All the other unknown errors can be handled by this exception handler
        except Exception as e:
            print('General exception handler')
            print('Error : {}'.format(e))
            logger.error(e)

        else:
            print('Congratulations!, No Exceptions occured')

        count += 1
        print('\n')
        

if __name__ == '__main__':
    # Create and configure logger
    logging.basicConfig(filename="code_exec.log",
                        format='%(asctime)s %(message)s',
                        filemode='a')

    # Creating an object
    logger = logging.getLogger()

    # Setting the threshold of logger to DEBUG
    # All the logging more severe than DEBUG will be saved in above file
    logger.setLevel(logging.DEBUG)

    # Case - 1 beginning
    logger.info('Started Execution : Case 1')
    count = int(input('Enter the count :'))
    get_squared_list(count)
    logger.info('Execution ended : Case_1')


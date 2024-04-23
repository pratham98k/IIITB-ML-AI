'''Map Function
Description
Using the Map function, create a list 'cube', which consists of the cube of numbers in input_list.

For e.g. if the input list is [5,6,4,8,9], the output should be [125, 216, 64, 512, 729]. '''

input_list=[5,6,4,8,9]

#solution one
#def cuben(n):
#    return n * n * n
#cube = map(cuben, input_list)
#print(list(cube))
#solution two
print(list(map(lambda x : x**3, input_list)))

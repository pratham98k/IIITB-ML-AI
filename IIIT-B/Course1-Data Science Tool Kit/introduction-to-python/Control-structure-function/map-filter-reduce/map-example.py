def cuben(n):
    return n*n*n

input_list=[5,6,4,8,9]

results= map(cuben, input_list)
print(list(results))
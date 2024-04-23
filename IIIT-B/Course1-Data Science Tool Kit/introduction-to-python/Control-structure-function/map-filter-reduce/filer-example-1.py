input_list=[ ['Ankur','Avik','Kiran','Nitin'],['Narang','Sarkar','R','Sareen']]

first_name=input_list[0]
last_name=input_list[1]

name= lambda x, y : x[0:] + ' ' + y[0:]
print(list(map(name, first_name, last_name)))
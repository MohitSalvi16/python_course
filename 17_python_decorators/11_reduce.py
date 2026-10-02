from functools import reduce

number=[2,32,4,1,14,2]

def sum(a,b):
    return a+b

new_list=reduce(sum,number)

print(new_list)





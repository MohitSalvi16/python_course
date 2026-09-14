def sum(a,b):
    print("this is the sum")
    c=a+b
    global z
    z=3
    return c

z=8
print(sum(4,5))
print(z)
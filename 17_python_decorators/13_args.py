def sum(*args):
    print(args)
    sum=0
    for item in args:
        sum=sum+item
    return sum

print(sum(2,3,55))

def safe_divide(a,b):
    if(b==0):
        print("Cannot divide by zero")
    return a//b

print(safe_divide(11,0))
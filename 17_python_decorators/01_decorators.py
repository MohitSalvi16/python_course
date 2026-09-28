def decorator(func):

    def wrapper():
        print("This is a funciton i have writte")
        func()
        print("this is after the function")
    return wrapper
    
@decorator
def say_hello():
    print("Hello")

say_hello()

# f=decorator(say_hello)

# f()
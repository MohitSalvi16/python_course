def marks(**kwargs):
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(harry=34,shubham=32,riya=56,john=99)


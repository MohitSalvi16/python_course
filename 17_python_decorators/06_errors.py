# while True:
#     try:
#         a=int(input("Enter number 1: "))
#         b=int(input("Enter number 2: "))

#         print(f"the division is {a/b}")

#     except ValueError:
#         print("Please don't perform the operation")

#     except ZeroDivisionError:
#         print("Don't divide by zero")

#     except Exception as e:
#         print("Some error comes",e)


a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
if b==0:
    raise ValueError("Please don't divide by zero")
print(f"the division is {a/b}")
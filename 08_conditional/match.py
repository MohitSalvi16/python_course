a=int(input("enter a lucky number from 1 to 10:"))

match a:
    case 1:
        print("You won a car")
    case 3:
        print("you won a smartphone")
    case 4:
        print("you won a toffee")
    case _:
        print("Better luck next time")
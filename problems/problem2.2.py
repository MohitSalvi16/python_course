num1= int(input("enter the first number: "))

num2=int(input("enter the second number: "))


operator= input("enter what need to be done: ")

match operator:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    

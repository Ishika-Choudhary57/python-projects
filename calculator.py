# Calculator:
try:
    print("Welcome to the calculator enter the vlaues to do the operation.")
    num = int(input("Enter a number here : "))
    num2 = int(input("Enter another number : "))
    sign = input("Enter the sign here : ")


    if (sign == "+"):
        print(f"The sum of {num} and {num2} is {num + num2}")
    elif(sign == "-" ):
        print(f"The ddifference of {num} and {num2} is {num - num2}")
    elif(sign == "*"):
        print(f"The multiplication of {num} and {num2} is {num + num2}")
    elif(sign == "/"):
        print(f"The division of {num} and {num2} is {num/num2}")
    else:
        print("enter a valid sign.")
except ValueError:
    print("Enter a valid value.")
else:
    print("Calculation is finished.")
finally:
    print("Thank You!")

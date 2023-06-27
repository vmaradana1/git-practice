number1 = float(input("Enter Number 1 :"))
number2 = float(input("Enter Number 2 :"))
print ("Calculator Menu :")
print( "ADD + \n SUBTRACT - \n MULTIPLY * \n DIVIDE / \n  SQUARE s")
operation = input ("Enter Operation : ")
if operation == "+":
    Sum = number1 + number2
    print (f"SUM is {Sum}")
elif operation == "-":
    differnce = number1 - number2
    print (f"differnce is {differnce}")
elif operation == "*":
    multiply = number1 * number2
    print (f"multiply is {multiply}")
elif operation == "/":
    division = number1 / number2
    print (f"division is {division}")
elif operation == "S":
    square = number1 ** number2
    print (f"square is {square}")
else:
    print("wrong operation")
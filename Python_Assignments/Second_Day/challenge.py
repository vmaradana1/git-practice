num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=int(input("Enter Third Number:"))

if (int(num1) > int(num2) and int(num3)):
    print(num1)
    if ((num1/2) == 0):
        print(f"max number is num1 : {num1} and its even ")
    elif((num1/3)== 0):
        print(f"max number is num1 : {num1} and its odd and multiple of 3 ")
    else:
        print(f"max number is num1 : {num1} and its odd")       
elif (int(num2) > int(num1) and int(num3)):
    print(num2)
    if ((num2/2) == 0):
        print(f"max number is num2 : {num2} and its even ")
    elif((num2/3)== 0):
        print(f"max number is num2 : {num2} and its odd and multiple of 3 ")
    else:
        print(f"max number is num2 : {num2} and its odd")
elif (int(num3) > int(num1) and int(num2)):
    print(num3)
    if ((num3/2) == 0):
        print(f"max number is num3 : {num3} and its even ")
    elif((num3/3)== 0):
        print(f"max number is num3 : {num3} and its odd and multiple of 3 ")
    else:
        print(f"max number is num3 : {num3} and its odd")
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=int(input("Enter Third Number:"))

if num1 > num2 and num3:
    print(num1)
    if ((num1 /2) ==0):
        print(f"max number is num1 : {num1} and its even ")
    elif((num1/3)==0):
        print(f"max number is num1 : {num1} and its odd and multiple of 3 ")
    else:
        print(f"max number is num1 : {num1} and its odd")       
elif num2 >num1 and num3:
    print(num2)
    if ((num2 /2) ==0):
        print(f"max number is num1 : {num2} and its even ")
    elif((num2/3)==0):
        print(f"max number is num1 : {num2} and its odd and multiple of 3 ")
    else:
        print(f"max number is num1 : {num2} and its odd")
elif num3 > num1 and num2:
    print(num3)
    if ((num3 /2) ==0):
        print(f"max number is num1 : {num3} and its even ")
    elif((num3/3)==0):
        print(f"max number is num1 : {num3} and its odd and multiple of 3 ")
    else:
        print(f"max number is num1 : {num3} and its odd")
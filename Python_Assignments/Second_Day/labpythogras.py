print ("Pythogras Menu :")
print( "Find Length of A given B & C 1 + \n Find Length of B given A & C 2 \n Find Length of C given A & B 3 ")
option = input ("Enter option : ")
if option == "1":
    B =int(input("Enter value for B : "))
    C =int(input("Enter value for C : "))
    output = (((C**2)-(B**2))**(1/2))
    print (f"A value is  is {output}")
elif option == "2":
    A =int(input("Enter value for A : "))
    C =int(input("Enter value for C : "))
    output = (((A**2)-(C**2))**(1/2))
    print (f"B value is  is {output}")
elif option == "3":
    A =int(input("Enter value for A : "))
    B =int(input("Enter value for B : "))
    output = (((A**2)-(B**2))**(1/2))
    print (f"C value is  is {output}")
else:
    print("wrong operation")
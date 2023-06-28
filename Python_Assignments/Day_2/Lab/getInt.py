min =int(input("Enter Min Number : "))
max =int(input("Enter Max Number : "))
a = int (input("Enter User value : "))
range =1 
if a > min and a < max:
    print(f"user entered value is {a}")
else:
    while range < 3:
        a = int (input("Enter User value : "))
        range =range + 1
    print(None)
    #print(f"User has Eneterd None")

    
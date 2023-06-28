
mark = int(input("Please Enter Your Marks :"))
level = int(input ("please enter student level :"))
if (level == 1):
    if mark > 70:
        print("Distinction")
    elif mark > 60:
        print("Merit")
    elif mark > 50:
        print("Pass")
    elif mark < 50:
        print("FAIL")
    else:
        print ("Error: marks between 1 and 100")
else:     
    if (level == 2):
        if mark > 65:
            print("Distinction")
        elif mark > 50:
            print("Merit")
        elif mark > 40:
            print("Pass")
        elif mark < 40:
            print("FAIL")
    else:
        print ("Error: marks between 1 and 100")
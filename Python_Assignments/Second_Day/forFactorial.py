number=int(input("Enter number :"))
increment=1
for a in range (1,number+1):
    increment = a * increment
print (f"Factorial for {number} is : {increment}")
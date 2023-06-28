number=int(input("Enter number :"))
increment = 1
factorial = number
while increment < number:
    factorial = factorial * increment
    increment+=1
print(f"Factorial of {number} is : {factorial} ")
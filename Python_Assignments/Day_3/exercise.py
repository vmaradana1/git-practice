def addition(num1,num2):
    x = num1 + num2
    return (f"Sum is : {x}")
num1 = int(input("Enter first number :" ))
num2 = int(input("Enter Second number :" ))
sum=addition(num1,num2)
print(sum)
print(addition(num1,num2))

# args 

def numbers_list(*numbers):
    for i in numbers:
        print(i)

numbers_list(1,2,3,4,5)

# def addition1(*numbers):




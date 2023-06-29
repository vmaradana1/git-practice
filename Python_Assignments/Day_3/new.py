def security(password):
    plist=("password","password1","password2")
    length=len(plist)
    for i in range (0,length):
        newpassword = plist[i]
        if {newpassword} == {password}:
                print(f"Not Accepted as it matches with standard password {plist[i]}")
                return
    
    print ("Password Accepted")  
    
password = input("Please Enter Password : ")
password1=security(password)
#print(password1)


def calc(num1,num2):
    x = num1 + num2
    
    return (f"Sum is : {x}")
num1 = int(input("Enter first number :" ))
num2 = int(input("Enter Second number :" ))
sum=addition(num1,num2)
print(sum)
print(addition(num1,num2))
# write an application that checks the strength of a password.
# Requirements:
# 
# Write a class that has a method that checks the password strength.
# Use factors like length, upper/lower case and if it has a number and special character.
# ratings hould be very weak - weak - moderate - strong - very strong 
# Check against a list of common passwords 10-20 common password = very weak
# User input that loops until the user quits
# A dictionary that returns a history of passwords/strengths whilst in the loop.



class Verify_Password:
    def __init__(self, password):
        self.password = password
        self.password_strength = password_strength
        
    def checklength(self,password):
        if len(password) > 6 and len(password) < 10 :
            self.password_strength += 1
        elif len(self.password) < 10:
            self.password_strength += 1
        else:
            self.password_strength = 0   
            #return False  

    def checkalpha(password):
        if password.isalpha() == True:
            #password_strength += 1
           return True
            
        elif password.isnumeric() == True:
            #password_strength += 1
            return True
        elif password.isalnum() == True:
            #password_strength += 1
            return True
        elif password.isnumeric() and password.isalpha() and password.isalnum() == True:
            #password_strength += 1
            return True
        elif password.isnumeric() and password.isalpha() == True:
            #password_strength += 1
            return True
        else:
            #password_strength =0
            return False

    def checkcase(self,password):
        if password.islower():
            return True
        elif password.isupper():
            return True
        elif password.islower() and password.isupper():
            return True
        else:
            return False 

password_strength =0 

userpassword= input("Enter Password: ")

while True:
    if len(userpassword) > 0:
        check1=Verify_Password.checklength(userpassword)
        if check1 is True:
            #password_strength=+1
            print (f"Counter for length : {password_strength}")
            break
        #check2 = Verify_Password.checkalpha(userpassword)
        #if check2 is True:
            #password_strength=+1
            print (f"Counter for Alpha: {password_strength}")
            #break
        
        #check3 = Verify_Password.checkcase(userpassword)
        #if check3 is True:
            
        else:
            print("Meesage needs to be changed")
            break
        
    
    
    
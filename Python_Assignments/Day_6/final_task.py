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
        
    #password_strength = 0

    def checklength(password):
        password_strength = 0 
        if len(password) > 6:
            return True
            #password_strength += 1
        else:
            return False
            #password_strength = 0
        

    def checkalpha(password):
        if password.isalpha() == True:
            password_strength += 1
        elif password.isnumeric() == True:
            password_strength += 1
        elif password.isalnum() == True:
            password_strength += 1
        elif password.isnumeric() and password.isalpha() and password.isalnum() == True:
            password_strength += 1
        elif password.isnumeric() and password.isalpha() == True:
            password_strength += 1
        else:
            password_strength =0
            
''''       
    def checkstandard(self,password):
        pass
    
    def checkcase(self,password):
        if password.islower():
            return 1
        elif password.isupper():
            return 2
        elif password.islower() and password.isupper()
            return 3
        else:
            return False 
'''
    
password_strength=0

userpassword= input("Enter Password: ")

while True:
    if len(userpassword) > 0:
        check1 = Verify_Password.checklength(userpassword)
        #check2 = Verify_Password.checkalpha(userpassword)
        #check3 = Verify_Password.checkstandard(userpassword)
        #check4 = Verify_Password.checkcase(userpassword)
    print (password_strength)
        
        
    
    
    
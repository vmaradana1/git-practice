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
        self.password_strength = 0
        
    def checklength(self,password):
        if len(password) > 6 and len(password) < 10 :
            self.password_strength += 1
        elif len(password) < 10:
            self.password_strength += 1
        else:
            self.password_strength = 0   
            

userpassword= input("Enter Password: ")

while True:
    if len(userpassword) > 0:
        check1=Verify_Password(userpassword)
        check1.checklength(userpassword)
        print (f"Counter for length : {check1.password_strength}")
    else:
        print("Meesage needs to be changed")
    break
        
    
    
    
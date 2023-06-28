userinput = (input("Enter String : "))
strlen = len(userinput)
#print(strlen)
strcounter =0
rangecounter= 0 
#print(type(userinput[1]))
while rangecounter < strlen:
    temp=userinput[rangecounter]
    #if (temp == 'e') or (temp == 'a') or (temp == 'i') or (temp == 'o') or (temp == 'u') :
    if temp in ['a','e','i','o','u']:
        strcounter=strcounter+1
    rangecounter=rangecounter+1
    
print(f"occurences of vowel is : {strcounter}")


    
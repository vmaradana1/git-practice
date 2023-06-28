userinput = (input("Enter String : "))
strlen = len(userinput)
#print(strlen)
strcounter =0
rangecounter= 0 
for a in range (1,strlen):
    temp = userinput[a]
    if temp in ['a','e','i','o','u']:
        strcounter=strcounter+1
print(f"occurences of vowel is : {strcounter}")
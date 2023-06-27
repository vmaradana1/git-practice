#mark = int(input("Please Enter Your Marks :"))
#mark = input("Please Enter Your Marks :")
#if mark.isalpha():
 #   print("Enter Number only")
  #  mark = int(input("Please Enter Your Marks :"))
   # if mark > 85:
    #    print ("Distinction")
    #elif mark > 65:
    #    print ("Pass")
    #else:
    #    print("Fail")
#else:
 #   if int(mark) > 85:
#        print ("Distinction")
#    elif int(mark) > 65:
#        print ("Pass")
#    else:
#        print("Fail")


weight = float(input("please enter weight : "))
measurment = input ("enter kgs or lbs : ")
cmeasurment = measurment.lower()
print(cmeasurment)

if cmeasurment == "kgs" :
    cweight = 2.2 * weight
    print(f"Converted Pounds is {cweight}")
elif cmeasurment == "lbs":
    cweight = (weight)/2.2
    print(f"Converted KGS is {cweight}")
else:
    print ("measurment is wrong")


# challenge:
# weight converter app: convert a user inputted weight(float), and user
# to select either kgs and lbs. write an if statement that checks 
# if the unit is kgs or lbs, if kgs convert into lbs and print the converted value.
# else: to handle the other way around. Error handling for upper/lower case. 

weight = float(input("Enter weight: "))
unit = input("K (Kgs) or L (Lbs): ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in Lbs: ", converted)
else: 
    converted = weight * 0.45
    print("weight in kgs: ", converted)


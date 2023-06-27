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

intialinvestment = int(input ("Enter Intial Investment : "))
IntresetRate = int(input ("Enter IntresetRate : "))
TragetValue = int(input ("Enter TragetValue : "))
#intialinvestment=100
#IntresetRate = 10
NumberofYears = 1

while intialinvestment < TragetValue :
    #print(f"intialinvestment : {intialinvestment}")
    newamount = (intialinvestment * IntresetRate)/100
    #print(f"newamount : {newamount}")
    intialinvestment=intialinvestment+newamount
    #print(f"intialinvestment after calculation :{intialinvestment}" )
    NumberofYears = NumberofYears + 1
    #print(NumberofYears)
    if (intialinvestment>=TragetValue):
        break

print(f"Number of {NumberofYears} years to reach 1000")
    
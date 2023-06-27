#intialinvestment = input ("Enter Intial Investment : ")
#IntresetRate = input ("Enter IntresetRate : ")
#TragetValue = input ("Enter TragetValue : ")
intialinvestment=100
IntresetRate = 10
NumberofYears = 1

while intialinvestment < 1000 :
    #print(f"intialinvestment : {intialinvestment}")
    newamount = (intialinvestment * 10)/100
    #print(f"newamount : {newamount}")
    intialinvestment=intialinvestment+newamount
    #print(f"intialinvestment after calculation :{intialinvestment}" )
    NumberofYears = NumberofYears + 1
    #print(NumberofYears)
    if (intialinvestment>=1000):
        break

print(f"Number of {NumberofYears} years to reach 1000")
    
intialinvestment = int(input ("Enter Intial Investment : "))
IntresetRate = int(input ("Enter IntresetRate : "))
TragetValue = int(input ("Enter TragetValue : "))
#intialinvestment=100
#IntresetRate = 10
NumberofYears = 1

while intialinvestment < TragetValue :
    newamount = (intialinvestment * IntresetRate)/100
    intialinvestment=intialinvestment+newamount
    NumberofYears = NumberofYears + 1
    if (intialinvestment>=TragetValue):
        break

print(f"Number of {NumberofYears} years to reach 1000")
    
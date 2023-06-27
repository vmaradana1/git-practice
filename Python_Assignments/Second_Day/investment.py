#intialinvestment = input ("Enter Intial Investment : ")
#IntresetRate = input ("Enter IntresetRate : ")
#TragetValue = input ("Enter TragetValue : ")
intialinvestment=100
IntresetRate = 0.1
NumberofYears = 1

while intialinvestment < 1000 :
    newcalculation = intialinvestment * IntresetRate
   # print(newcalculation)
    intialinvestment=intialinvestment+newcalculation
   # print(intialinvestment)
    NumberofYears = NumberofYears + 1
   # print(NumberofYears)
    if (intialinvestment>=1000):
        break

print(f"Number of {NumberofYears} years to reach 1000")
    
#intialinvestment = input ("Enter Intial Investment : ")
#IntresetRate = input ("Enter IntresetRate : ")
#TragetValue = input ("Enter TragetValue : ")
intialinvestment=100
IntresetRate = 0.1
NumberofYears = 1

while NumberofYears > 1:
    intialinvestment = intialinvestment * IntresetRate
    NumberofYears +1
    if (intialinvestment>1000):
        break
    print(f"Number of {NumberofYears} to reach 1000")
    
def tax_calc(updatedsal):
    print (f"This is after coming in to loop :{updatedsal}")
    if updatedsal > 0 and updatedsal <= 34500:
        updatedsal = ((updatedsal * 20)/100)
        return updatedsal
    elif 34501 <= updatedsal <= 150000:
        updatedsal = 4350 + ((updatedsal-34500)* 0.4)
        return updatedsal
    else:
        updatedsal = 50000 + ((updatedsal-150000)* 0.45)
        return updatedsal    

sal = int(input("Enter your Salary:" ))
updatedsal = sal - 11500
if updatedsal <= 0:
    print("you have no tax ENJOY !!!!")
else:
    updatedsal=tax_calc(updatedsal)
    print (f"TAX for your salary is : {updatedsal}")
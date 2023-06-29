def tax_calc(updatedsal):
    print (f"This is after coming in to loop :{updatedsal}")
    if updatedsal > 0 and updatedsal < 34500:
        updatedsal = ((updatedsal * 20)/100)
        return updatedsal
    elif 34501 < updatedsal < 150000:
        updatedsal = (updatedsal * 40)/100
        return updatedsal
    else:
        updatedsal = (updatedsal * 45)/100
        return updatedsal    

sal = int(input("Enter your Salary:" ))
updatedsal = sal - 11500
if updatedsal <= 0:
    print("you have no tax ENJOY !!!!")
else:
    updatedsal=tax_calc(updatedsal)
    print (f"TAX for your salary is : {updatedsal}")
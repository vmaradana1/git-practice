# Python program to read CSV file line by line
# import necessary packages
import csv
companies = []
sales = []

with open('carsale.csv') as csvfile: # dont need r/w attribiute for csv 
    reader = csv.reader(csvfile)
    next(reader) # skipping header 
    for row in reader: #row is variable:
        companies.append(row[0])
        sales.append([int(x.replace(",",""))for x in row[1:]])
        
print(sales[1])
total = 0
for num in sales[1]:
    total += num

print(total)


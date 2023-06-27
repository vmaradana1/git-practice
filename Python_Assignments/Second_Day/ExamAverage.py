english=int(input("Enter english Marks between 0 and 100 : "))
while english > 100 or english < 0:
    english=int(input("Enter english Marks between 0 and 100 : "))
else:
    if english >= 65:
        print(f"English PASSED")
    else:
        print(f"English FAILED")
maths=int(input("Enter maths Marks between 0 and 100 : "))
while maths > 100 or maths < 0:
    maths=int(input("Enter maths Marks between 0 and 100 : "))  
else:
    if maths >= 65:
        print(f"maths PASSED")
    else:
        print(f"maths FAILED")     
ict=int(input("Enter ict Marks between 0 and 100 : "))
while ict > 100 or ict < 0:
    ict=int(input("Enter ict Marks between 0 and 100 : "))       
else:
    if ict >= 65:
        print(f"ICT PASSED")
    else:
        print(f"ICT FAILED")   
        
total = english+maths+ict
average = total/3
print(f'total marks is : {total}')
print(f'average marks is : {average}')
if average >= 65:
    print(f"STUDENT PASSED with average of : {average}")
else:
      print(f"STUDENT FAILED with average of : {average}")
  


    

newlist=[]
time1 = input("Enter Time 1 DD:HH:MM : ")
x=time1.split(":")
for b in range(0, len(x)):
    x[b] = int(x[b])
 
time2 = input("Enter Time 2 DD:HH:MM : ")
y=time2.split(":")
for d in range(0, len(y)):
    y[d] = int(y[d])




#print(f"Main Menu \n Option 1 - Add 2 Times ")
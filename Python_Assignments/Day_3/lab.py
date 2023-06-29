import statistics
data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

#grades=data.split(",")
#grades = list(map(int, grades))
#data = [int(data) for data in data.split(",") ]
grades = [int(data) for data in data.split(",") ]
#grades = [int(grades) for grades in data.split(",") ]

print(data)
#grades = [int(grades) for grades in data.split(",") ]
print(grades)
mingrade=min(grades)
print(f"Min Grade is : {mingrade}")
maxgrade=max(grades)
print(maxgrade)
total=sum(grades)
print(total)
length1=len(grades)
print(length1)
average1= round(total/length1,2)
print(average1)
median1=statistics.median(grades)
print(median1)

output = "Minimum grade : {}\nMax Grade : {}"
print(output.format(mingrade, maxgrade))

print("Minimum Grade : {}\nMax Grade : {}".format(mingrade, maxgrade))
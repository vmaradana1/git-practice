class Students:
    def __init__(self,name,age):
        self.name= name
        self.age = age

        
student1= Students('Vamsi', 23)
student2=Students('Test', 43) 

print(f"Student 1 name is : {student1.name}")
print(f"Student 1 Age is : {student1.age}")


class Students1:
    def __init__(self,name,age):
        self.name= name
        self.age = age
        
    def class_(self):
        class_=input("Enter your Current Class: ")
        return class_
    
    def AverageMarks(self):
        mark1=int(input(f"Enter Marks 1: "))
        mark2=int(input(f"Enter Marks 2: "))
        mark3=int(input(f"Enter Marks 3: "))
        averageMark= (mark1+mark2+mark2)/3
        return averageMark
    
    def AverageMarks1(self,mark1,mark2,mark3):
        averageMark= (mark1+mark2+mark3)/3
        return averageMark
        
        
student3= Students1('Vamsi', 23)
AverageMarks2=student3.AverageMarks1(25,25,25)
student4=Students1('Test', 43) 

print(f"Student 3 name is : {student3.name}")
print(f"Student 3 Age is : {student3.age}")
print(f"Student 3 Current Class is :{Students1.class_(student3)}")
print(f"Student 3 Average Marks are : {AverageMarks2}")
print(f"Student 3 Average Marks for inputted Marks : {Students1.AverageMarks(student3)}")

class Bird:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wingspan} cm")

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"
    
class Owl(Bird):
    def __init__(self, name, wingspan, nocturnal=True):
        super().__init__(name, wingspan)
        self.nocturnal = nocturnal

    def hoot(self):
        print(f"{self.name} is hooting")

    def __str__(self):
        return super().__str__() + f" - noctunal: {self.nocturnal}"
    
class Dodo(Bird):
    def __init__(self, name, wingspan, extinct=True):
        super().__init__(name, wingspan)
        self.extinct = extinct

    def __str__(self):
        return super().__str__() + f" - extinct: {self.extinct}"
    
bird1 = Bird("eagle", 20)
owl1 = Owl("barn owl", 90)
dodo1 = Dodo("the dodo", 100)

bird1.fly()
print(bird1)

owl1.fly()
print(owl1)

dodo1.fly()
print(dodo1)
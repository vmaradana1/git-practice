#1. Create a Rectangle class with attributes length and width. 
#Add methods to calculate the area and perimeter of the rectangle. 

"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimiter(self):
        return 2 * (self.length * self.width)
    
rect = Rectangle(5, 10)
print(rect.area())
print(rect.perimiter())


#2. Create a BankAccount class with attributes account_number and balance. 
#Add methods to deposit and withdraw money from the account. 

class BankAccount:
    def __init__(self,account_number,depositbalance=0):
        self.account_number = account_number
        self.depositbalance = depositbalance
    
    def deposit(self,depositamount):
        self.depositbalance += depositamount
        return depositamount
    
    def withdraw(self,withdrawlamount):
        self.depositbalance -= withdrawlamount
        return withdrawlamount
        
    def displaybalance(self):
        return self.depositbalance
     
bankdetails=BankAccount(23)
balancebeforedeposit=bankdetails.deposit(1000)
balanceafteredeposit=bankdetails.displaybalance()
balancebeforewithdrawl=bankdetails.withdraw(500)
balanceafterwithdrawl=bankdetails.displaybalance()

print(f"New Account balance after depositing {balancebeforedeposit} is : {balanceafteredeposit}")
print(f"New Account balance after withdrawing {balancebeforewithdrawl} is : {balanceafterwithdrawl}")


#3. Create a Car class with attributes make, model, and year. 
#Add methods to get and set the values of the attributes. 

class Car:
    def __init__(self,model,make,year):

        self.model = model
        self.make = make
        self.year = year
            
    def get_make(self):  
        return self.make
    
    def get_model(self):  
        return self.model
    
    def get_year(self):  
        return self.year
    
    def set_make(self,updatedmake):
        self.make=updatedmake
    
    def set_model(self,updatedmodel):
        self.model=updatedmodel              
    
    def set_year(self,updatedyear):
        self.year=updatedyear    
        
car1=Car('model1','make1',2009)
print(car1.get_make())
car1.set_make("make11")
print(car1.get_make())
   

    

#4. Create a Product class with attributes name, price, and quantity. 
#Add methods to calculate the total value of the product (price * quantity) 
#and add or remove items from the product inventory. 

class Product:
    def __init__(self,name,price=0,quantity=0):
        self.name=name
        self.price=price
        self.quantity=quantity
    
    def tvalue(self):
        totalvalue = self.price * self.quantity
        return totalvalue
    
    def addproducts(self,addquantity):
        addquantity = self.quantity+addquantity
        return addquantity
    
    def removeproducts(self,removequantity):
        removequantity = self.quantity - removequantity
        return removequantity
    

items = Product("Test",10,100)
#print(f"Total value is : {items}")

Totalvalue=items.tvalue()  
print(f"Total value is : {Totalvalue}")

AddQuantity=items.addproducts(10)
print(f"Total updated Quantity is : {AddQuantity}")

removedQuantity=items.removeproducts(10)
print(f"Total updated Quantity is : {removedQuantity}")

"""

#Harder challenge (stretch goal): 

#Create a Book class and BookShelf class that can be used to manage a collection of books. 
#Create a Book class that has the following attributes: 
#title (str), author (str), publisher (str), publication year (int). 
#The class should also have a str method that returns the book's information in a 
#formatted string. 
#Create a BookShelf class that has the following attributes: 
#capacity (int), list of books (list). 
#The class should have the following methods: 
#- add_book: adds a book to the list of books if the shelf is not full 
#- remove_book: removes a book from the list of books if it exists on the shelf 
#- find_book_by_title: searches for a book by its title 
#and returns the book object if found 
#- find_books_by_author: searches for books by a specific author 
#and returns a list of book objects if found 
#The class should also have a str method that returns a string representation 
#of the books on the shelf. 

class Book:
    def __init__(self,title,author,publisher,publicationyear):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publicationyear = publicationyear
        
class BookShelf:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.bookslist = []
    
    def add_book(self,book):
        if len(self.bookslist) < self.capacity:
            self.bookslist.append(book)
            print(f"{book.title} has been added")
        else:
            print ('SHELF is FULL')
            
    def remove_book(self,book):
        if book in self.bookslist:
            self.bookslist.remove(book)
            print(f"{book.title} has been removed")
        else:
            print('Book doesnt exist')     
            
 #method find book by author 

 #method find book by title 
 
    def __str__(self):
        if not self.bookslist:
            return "Shelf is Empty"
        else:
            output = "Books on the SHELF : \n "
            for book in self.bookslist:
                output += str(book) + "\n\n"
            return output
        
book1 = Book('title1','author1','publisher1',2009)
bookshelf = BookShelf(4)
print(bookshelf)
bookshelf.add_book(book1)
bookshelf.remove_book(book1)

        
    

#Create four Book objects and add them to a BookShelf object with a capacity of three. 
#Test the BookShelf object by adding, removing, and finding books by title and author.
#Print the BookShelf object after each action.

#Alternative stretch goal: rewrite the rock/paper/scissor app using a class. 
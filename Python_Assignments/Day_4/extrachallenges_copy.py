class Book:
    def __init__(self,title,author,publisher,publicationyear):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publicationyear = publicationyear
        
    def __str__(self):
        return (f"title : {self.title} \n author: {self.author} \n publication : {self.publisher} \n year : {self.publicationyear} ")
       
        
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
            
    def __str__(self):
        if not self.bookslist:
            return "Shelf is Empty"
        else:
            output = "Books on the SHELF : \n "
            for book in self.bookslist:
                output += str(book) + "\n\n"
            return output
    
#method find book by author 
    def find_book_author(self,book,checkauthor):
        for book in self.bookslist:
            if checkauthor == book1.author:
                output1= (f"{book1.author} book exists \n related book details are as follows")
                output1 += str(book) + "\n\n"
                print (output1)
            else:
                print (f"{book1.author} book doesn't exists")

 #method find book by title
    def find_book_title(self,book,checktitle):
        for book in self.bookslist:
            if checktitle == book1.title:
                output2= (f"{book1.title} related book exists \n related book information are as follows : \n")
                output2 += str(book) + "\n\n"
                print (output2)

            else:
                print (f"{book1.title} related book doesn't exists")

        
book1 = Book('title1','author1','publisher1',2009)
book2 = Book('title2','author2','publisher2',2019)
"""book3 = Book('title3','author3','publisher3',2029)
book4 = Book('title4','author4','publisher4',2039)"""


bookshelf = BookShelf(4)

for i in range(1,2):    
    bookshelf.add_book(book1)

"""checkauthor=book1.author
checkauthor = input(f"Author to find : ")
bookshelf.find_book_author(book1,checkauthor)
checktitle=book1.title
checktitle = input(f"Title to find : ")
bookshelf.find_book_title(book1,checktitle)
#bookshelf.remove_book(book1)
#bookshelf.find_book("title1")



        
    

#Create four Book objects and add them to a BookShelf object with a capacity of three. 
#Test the BookShelf object by adding, removing, and finding books by title and author.
#Print the BookShelf object after each action.

#Alternative stretch goal: rewrite the rock/paper/scissor app using a class. """
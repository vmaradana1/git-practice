books = {"a1": ["b11","b12"], "a2": ["b21","b22","b23"], "a3": ["b31","b32","b33"]}
author= input("Enter Author Name: ")
print (author)
print (", ".join(books[author]))
print (", ".join(books.get(author)))
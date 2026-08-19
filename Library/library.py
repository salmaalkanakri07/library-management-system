import json
with open("books.json","r") as books_file:
    books = json.load(books_file)

print("==== Library ====\n")

def find_book(book_name):
    for i in range (len(books)):
        if books[i]["Title"] == book_name:
            return i
    return -1
def add_book():
        Title = input("Enter book title: ").lower()
        Author = input("Enter Author: ").lower()
        book = {"Title" : Title,
                "Author" : Author,
                "Status" : "Available"}
        books.append(book)
        with open("books.json","w") as books_file:
            json.dump(books,books_file,indent = 4) 

def view_books():
        for book in books:
            print("Title:",book["Title"])
            print("Author:",book["Author"])
            print("Status:",book["Status"],"\n")
        if books == []:
            print("No Books Yet!")    

def search_book(book_name): 
        index = find_book(book_name)      
        if index != -1:
            for key,value in books[index].items():
                print(key,":",value)  
        else:
            print("Not Found!")

def borrow_book(book_name):
    index = find_book(book_name)      
    if index == -1:
        print("Not Found!") 

    elif books[index]["Status"] == "Available":
        books[index]["Status"] = "Borrowed"
        with open("books.json","w") as books_file:
            json.dump(books,books_file,indent = 4)

        print("The book you borrowed:")
        for key,value in books[index].items():                
            print(key,":",value) 
    elif books[index]["Status"] == "Borrowed":
        print("Already Borrowed!")  
         

              

def return_book(book_name):
    index = find_book(book_name)      
    if index == -1:
        print("Not Found!")        
    elif books[index]["Status"] == "Borrowed":
        books[index]["Status"] = "Available"
        with open("books.json","w") as books_file:
            json.dump(books,books_file,indent = 4)

        print("The book you returned:")
        for key,value in books[index].items():                
                print(key,":",value)
    elif books[index]["Status"] == "Available":
        print("The book was not borrowed!") 

def delete_book(book_name):
    index = find_book(book_name)
    if index == -1:
         print("Not Found!")
    else:      
        books.pop(index)
        with open("books.json","w") as books_file:
            json.dump(books,books_file,indent = 4)
        print("Deletion Done!")     

while True:
    print("\n1.Add Book")
    print("2.view Books")
    print("3.Search Book")
    print("4.Borrow Book")
    print("5.Return Book")
    print("6.Delete Book")
    print("7.Exit")
    option = input("\nChoose an option:")
    print(" ")
    if option == "1":
          add_book()   

    elif option == "2":
          view_books()   

    elif option == "3":
         book_name = input("Enter book title: ").lower()
         search_book(book_name)   

    elif option == "4":
         book_name = input("Enter a book title to borrow: ").lower()
         borrow_book(book_name)

    elif option == "5":
         book_name = input("Enter a book title to return: ").lower()
         return_book(book_name)  
    elif option == "6":
         book_name = input("Enter book title to delete: ").lower()
         delete_book(book_name)   
    elif option == "7":
         break          
    else:
        print("Invalid Option!")               
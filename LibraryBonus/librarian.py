import json

def load_library():
    try:
        with open("library.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
def save_library(library):
    with open("library.json", "w", encoding="utf-8") as file:
        json.dump(library, file, indent=4)
# Add
def add_book(library:dict):
    user_title = input("Enter the title: ")
    user_author = input("Enter the author: ")
    user_isbn = input("Enter the isbn: ")
    if user_isbn in library:
        print("There is a book with the same number ISBN.")
        return
        
    library[user_isbn]={
        "title" : user_title,
        "author" : user_author,
        "isbn" : user_isbn,
        "available":True
    }
    save_library(library)
    print("Book added successfully.")

# Display
def display_book(library:dict):
    if not library:
        print("No books in the library.")
        return
    for num, book in enumerate(library.values(),start=1):
        if book['available']==True:
            status = "Available"
        else:
            status = "Borrow"
        print(f"{num}-Title: {book['title']} by Author: {book['author']} (ISBN:{book['isbn']}) - {status}")
    return library    

# Search
def search_book(library: dict):
    choice = input("Search by title or author or ISBN: ").lower()
    found = False
    if choice == 'title':
        user_title = input("Enter the title: ")
        for book in library.values():
            if book['title'].lower() == user_title.lower():
                if book['available'] == True:
                    status = 'Available'
                else:
                    status = "Borrow"
                print(f"Title: {book['title']} by {book['author']} (ISBN:{book['isbn']}) - {status}")
                found =True
    
    elif choice == 'author':
        user_author = input("Enter the author: ")
        for book in library.values():
            if book['author'].lower() == user_author.lower():
                if book['available'] == True:
                    status = 'Available'
                else:
                    status = "Borrow"
                print(f"Title: {book['title']} by {book['author']} (ISBN:{book['isbn']}) - {status}")
                found =True

    elif choice == 'isbn':
        user_isbn = input("Enter the isbn: ")
        for book in library.values():
            if book['isbn'].lower() == user_isbn.lower():
                if book['available'] == True:
                    status = 'Available'
                else:
                    status = "Borrow"
                print(f"Title: {book['title']} by {book['author']} (ISBN:{book['isbn']}) - {status}")
                found =True
    else:
        print("Invalid choice.")
    if not found:
        print("Book not found.")
# Remove
def remove_book(library:dict):
    user_isbn_remove =input("Enter the isbn:")
    if user_isbn_remove not in library:
       print("The book is not found in the library.")
       return
       
    del library[user_isbn_remove]
    save_library(library)
    print("Book Removed successfully.")

# Borrow
def borrow_book(library:dict):
    user_isbn_borrow = input("Enter the isbn: ")
    if user_isbn_borrow not in library:
        print("The book is not found in the library.")
        return
        
    if not library[user_isbn_borrow]["available"]:
        print("The book is not available.")
        return
        
    library[user_isbn_borrow]["available"]= False
    save_library(library)
    print("Book checked out successfully.")

# Rerurn
def return_book(library:dict):
    user_isbn_return =input("Enter the isbn:")
    if user_isbn_return not in library:
        print("The book is not found in the library.")
        return
    library[user_isbn_return]["available"]= True
    save_library(library)
    print("Book Returned successfully.")
    
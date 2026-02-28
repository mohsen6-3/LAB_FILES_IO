from librarian import add_book,display_book,borrow_book,return_book,remove_book,search_book,load_library
library=load_library()

menu = (
'''
The Menu:
1. Add Book
2. Display Books
3. Search Book
4. Delete Book
5. Borrow Book
6. Return Book
7. Exit
'''
)
while True:
    print(menu)
    user_input= input("Choose one of the options:")

    if user_input == "1":
        # Add Book
        add_book(library)

        # display all book
    elif user_input == "2":
        display_book(library)

    elif user_input == "3":
        # search Book
        search_book(library)
        print()

    elif user_input == "4":
        # Remove Book
        remove_book(library)

    elif user_input == "5":
        # Borrow Book
        borrow_book(library)
        print()

    elif user_input == "6":
        # Return Book
        return_book(library)
        print()
        
        # Exit
    elif user_input =="7":
        print("Exiting the program. Goodbye!")
        break

    else:
         print("Invalid choice. Try again.")







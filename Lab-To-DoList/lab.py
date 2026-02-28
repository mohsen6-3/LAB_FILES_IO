# Solved the lab
def To_DoList():
    while True:
        user_input=input("Do you want to add a new To-Do item ? answer by (y/n) or (exit: Stop the program): ").lower()

        if user_input == "exit":
            print("Thank you for using the To-Do program, come back again soon.")
            break
            
        elif user_input =="y":
            user_input_item = input("Enter your new To-Do item: ")
            with open("to_do.txt","a",encoding="utf-8") as file:
                file.write(user_input_item+"\n")
                print("The addition is successfuly.")

        elif user_input =="n":
            user_input_list=input("Do you want to list your To-Do items ? answer by (y/n) :").lower()
            if user_input_list !="y" and user_input_list !="n":
                print("Invalid input. Please answer by (y/n).")
            elif user_input_list =="y":
                try:
                    with open("to_do.txt","r",encoding="utf-8") as file:
                        print("\nYour To-Do List:")
                        for num,line in enumerate (file):
                            print(f'{num+1}- {line.strip()}')
                        print()
                except FileNotFoundError:
                    print("The file not found.")
            elif user_input_list =="n" :
                print("You chose not to see the To-Do items. Returning to main menu.")
        else:
            print("Invalid input. Please answer by (y/n/exit).")
            
To_DoList()
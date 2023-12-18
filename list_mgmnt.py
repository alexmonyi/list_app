#define an empty list to store items
items=[]
# Defines a function to display the menu options.
def show_menu():
    #title for the application.
    print("\n**List App **\n")
    # print the menu options:
    print("1.Add item")
    print("2.Remove item")
    print("3. View List")
    print("4.Mark item as done")
    print("5. Exit")
    # Takes user input to choose an option from the menu and stores it in the variable choice
    choice=input("\nEnter your choice:")
    #Returns the user 's choice from the show_menu() function.
    return choice

#Initiates an infinite loop.
while True:
    choice=show_menu()
    if choice == "1":
        item = input("Enter New item")
        items.append(item)
    elif choice == "2":
        index= int(input("Enter item to remove:"))
        if index >= 0 and index < len(items):
            items.pop(index)
        else:
            print("Invalid index")
    elif choice == "3":
        if not items:
            print("List is empty!")
        else:
            for i,item in enumerate(items):
                print (f"{i+1}.{item}")

    elif choice == "4":
        index = int(input("Enter item index to mark done:"))
        if index >= 0 and index < len(items):
            items[index] = f"[DONE] {items[index]}"
        else:
            print("Invalid index")
    elif choice == "5":
        break
    else:
        print("Invalid choice")
print("\nExiting the app")


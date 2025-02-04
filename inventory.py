#dictionary to store item names and quatities
inventory = {}
#while loop to keep program running till user exits
while True : 

# Displays a Menu with options
    print("1 - Add item")
    print("2 - Get Item")
    print("3 - Total Items")
    print("4 - Exit")
   
# Takes user input to determine action 
    choice = input("Enter Choice: ")

#Adding items
    if choice == "1":     
        name = input("Item name: ")
        #converts the input to an integer
        quantity = int(input("Quantity: "))
        inventory[name] = inventory.get(name, 0) + quantity
#Displays the added name(keys) and Quantities(value)
        print("Added", quantity, name)

    elif choice == "2":
        #Asks for item name
        name = input("Item name: ")
        #Checks if item exists if not prints not found
        print(name, ":", inventory.get(name, "Not found"))
    
    elif choice == "3":
        #Sums up all inventory quantities(values) and prints number of items stored
        print("Total items:", sum(inventory.values()))
    
    elif choice == "4":
        #Exits the program
        print("Goodbye!")
        break
    
    else:
        #if user enters a number not within 1-4
        print("Invalid choice, try again.")


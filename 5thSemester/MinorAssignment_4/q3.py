lst = []
while True:
    print("\nMenu:\n1. Create a list\n2. Display list\n3. Insert element\n4. Delete element\n5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        lst = list(range(int(input("Enter the number of elements (N): "))))
        print("List created successfully.")
    elif choice == 2:
        print("List elements:", lst if lst else "The list is empty.")
    elif choice == 3:
        if lst:
            try:
                elem = int(input("Element to insert: "))
                pos = int(input("Position (0-based): "))
                lst.insert(pos, elem) if 0 <= pos <= len(lst) else print("Invalid position.")
            except ValueError:
                print("Enter valid integers.")
        else:
            print("Create a list first.")
    elif choice == 4:
        if lst:
            try:
                pos = int(input("Position to delete (0-based): "))
                print(f"Removed: {lst.pop(pos)}") if 0 <= pos < len(lst) else print("Invalid position.")
            except ValueError:
                print("Enter a valid integer.")
        else:
            print("Create a list first.")
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

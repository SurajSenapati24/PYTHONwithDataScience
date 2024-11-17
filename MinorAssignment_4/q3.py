
lst = []
while True:
    print("\nMenu:")
    print("1. Create a list of N integers")
    print("2. Display the list elements")
    print("3. Insert an element at a specific position")
    print("4. Delete an element at a given position")
    print("5. Exit")
    choice=int(input("Enter your choice: "))
    if choice == 1:
       N = int(input("Enter the number of elements (N): "))
       lst = [i for i in range(N)]
       print("List created successfully.")
    elif choice == 2:
        print("List elements:", lst if lst else "The list is empty.")
    elif choice == 3:
        if lst:
            try:
                element = int(input("Enter the element to insert: "))
                position = int(input("Enter the position (0-based index): "))
                if 0 <= position <= len(lst):
                    lst.insert(position, element)
                    print("Element inserted successfully.")
                else:
                    print("Invalid position.")
            except ValueError:
                print("Invalid input. Please enter valid integers.")
        else:
            print("The list is empty. Create a list first.")
    elif choice == 4:
        if lst:
            try:
                position = int(input("Enter the position (0-based index) to delete: "))
                if 0 <= position < len(lst):
                    removed_element = lst.pop(position)
                    print(f"Element {removed_element} removed successfully.")
                else:
                    print("Invalid position.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        else:
            print("The list is empty. Create a list first.")
    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

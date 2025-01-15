def write_to_file():
    file_name = input("Enter the name of the file to write (e.g., 'output.txt'): ")

    try:
        # Open the file in write mode
        with open(file_name, "w") as file:
            print("Enter the text you want to write into the file. Type 'STOP' to finish:")

            while True:
                user_input = input("> ")
                if user_input.strip().upper() == "STOP":
                    break
                file.write(user_input + "\n")

        print(f"Data successfully written to '{file_name}'.")

    except FileNotFoundError:
        print("Error: Unable to open or create the file.")
    except PermissionError:
        print("Error: Permission denied. Cannot write to the specified file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the program
write_to_file()

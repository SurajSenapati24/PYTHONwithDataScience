# Reading grades from grades.txt
try:
    with open('grades.txt', 'r') as file:
        grades = file.readlines()
    grades = [int(grade.strip()) for grade in grades]
    print("Individual Grades:", grades)
    total = sum(grades)
    count = len(grades)
    average = total / count if count > 0 else 0
    print(f"Total: {total}")
    print(f"Count: {count}")
    print(f"Average: {average:.2f}")
    
except FileNotFoundError:
    print("Error: File not found.")
except ValueError:
    print("Error: File contains invalid data.")



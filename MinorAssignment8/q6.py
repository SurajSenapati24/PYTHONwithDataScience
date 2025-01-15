import csv

# Open the CSV file in append mode
with open('grades.csv', mode='a', newline='') as file:
    writer = csv.writer(file)

    # Get student data from the instructor
    firstname = input("Enter the student's first name: ").strip()
    lastname = input("Enter the student's last name: ").strip()
    exam1 = int(input("Enter the grade for Exam 1: "))
    exam2 = int(input("Enter the grade for Exam 2: "))
    exam3 = int(input("Enter the grade for Exam 3: "))

    # Write the data to the CSV file
    writer.writerow([firstname, lastname, exam1, exam2, exam3])

print("Student data saved to 'grades.csv'!")

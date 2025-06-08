# Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
# Add a new student and grade.
# Update an existing student’s grade.
# Print all student grades.
student_grades = {}
def add_student():
    name=input("Enter Name:")
    if(name in student_grades):
        print("Student already exists. Use update option to change grade.")
    else:
        grade=input("Enter Grade:")
        student_grades[name] = grade
        print("Added" + name + "with"+ grade + "grade.")
def update_student():
    name=input("Enter Name:")
    if(name in student_grades):
        grade=input("Enter New Grade:")
        student_grades[name] = grade
        print("Updated"+ name +"with new grade"+ grade)
    else:
        print("Student not found. Use add option to create a new student.")
def print_grades():
    if student_grades:
        print("Student Grades:")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No student grades available.")

while True:
    print("\nOptions:")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Print All Grades")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        update_student()
    elif choice == '3':
        print_grades()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")
# Student Grades Management System

class StudentGrades:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if name in self.students:
            print(f"Student {name} already exists. Use update to change the grade.")
        else:
            self.students[name] = grade
            print(f"Student {name} with grade {grade} added successfully.")

    def update_grade(self, name, grade):
        if name in self.students:
            self.students[name] = grade
            print(f"Grade for student {name} updated to {grade}.")
        else:
            print(f"Student {name} does not exist. Use add to insert the student.")

    def delete_student(self, name):
        if name in self.students:
            del self.students[name]
            print(f"Student {name} deleted successfully.")
        else:
            print(f"Student {name} does not exist.")

    def view_students(self):
        if self.students:
            print("\nStudent Grades List:")
            for name, grade in self.students.items():
                print(f"Student: {name}, Grade: {grade}")
        else:
            print("No students found.")

# Main program loop
def main():
    grade_system = StudentGrades()

    while True:
        print("\n--- Student Grades Management System ---")
        print("1. Add Student")
        print("2. Update Student Grade")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                name = input("Enter student's name: ")
                grade = input("Enter student's grade: ")
                grade_system.add_student(name, grade)

            elif choice == 2:
                name = input("Enter student's name to update: ")
                grade = input("Enter new grade: ")
                grade_system.update_grade(name, grade)

            elif choice == 3:
                name = input("Enter student's name to delete: ")
                grade_system.delete_student(name)

            elif choice == 4:
                grade_system.view_students()

            elif choice == 5:
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()

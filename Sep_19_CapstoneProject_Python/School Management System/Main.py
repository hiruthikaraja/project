from student_module import load_students, print_students, find_topper, add_student
from teacher_module import load_teachers, print_teachers, average_salary, highest_paid_teacher, add_teacher
from reports import generate_report


def menu():
    while True:
        print("\n===== School Management System =====")
        print("1. View All Students")
        print("2. View All Teachers")
        print("3. Add New Student")
        print("4. Add New Teacher")
        print("5. Show Topper Student")
        print("6. Show Highest Paid Teacher")
        print("7. Show Average Teacher Salary")
        print("8. Generate Reports")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            students = load_students()
            print("\n--- Students ---")
            print_students(students)

        elif choice == "2":
            teachers = load_teachers()
            print("\n--- Teachers ---")
            print_teachers(teachers)

        elif choice == "3":
            students = load_students()
            try:
                new_id = int(input("Enter ID: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                grade = input("Enter Grade: ")
                math = int(input("Enter Math Marks: "))
                science = int(input("Enter Science Marks: "))
                english = int(input("Enter English Marks: "))

                new_student = {
                    "id": new_id,
                    "name": name,
                    "age": age,
                    "grade": grade,
                    "marks": {"Math": math, "Science": science, "English": english}
                }

                add_student(students, new_student)
            except ValueError:
                print(" Invalid input. Please enter numbers where required.")

        elif choice == "4":
            teachers = load_teachers()
            new_id = input("Enter ID: ")
            name = input("Enter Name: ")
            subject = input("Enter Subject: ")
            salary = input("Enter Salary: ")

            new_teacher = {"id": new_id, "name": name, "subject": subject, "salary": salary}
            add_teacher(teachers, new_teacher)

        elif choice == "5":
            students = load_students()
            find_topper(students)

        elif choice == "6":
            teachers = load_teachers()
            highest_paid_teacher(teachers)

        elif choice == "7":
            teachers = load_teachers()
            print(f"\nAverage Salary: {average_salary(teachers)}")

        elif choice == "8":
            generate_report()

        elif choice == "9":
            print(" Exiting School Management System. Goodbye!")
            break

        else:
            print(" Invalid choice. Please select between 1 and 9.")


if __name__ == "__main__":
    menu()

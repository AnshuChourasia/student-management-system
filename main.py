import json


def main():
    students=load_students()

    while True:
        print("Welcome to the Student Management System")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Search for a student")
        print("4. Update student details")
        print("5. Delete a student")
        print("6. Calculate average marks for a student")
        print("7. Find highest scorer")
        print("8. Total number of students")
        print("9. Grade Evaluation")
        print("0. Exit")

        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 1:
            add_student(students)
        elif option == 2:
            view_students(students)
        elif option == 3:
            try:
                student_id = int(input("Enter student ID to search: "))
            except ValueError:
                print("Invalid ID.")
                continue
            search_student(students, student_id)
        elif option == 4:
            try:
                student_id = int(input("Enter student ID to update: "))
            except ValueError:
                print("Invalid ID.")
                continue
            update_student(students, student_id)
        elif option == 5:
            try:
                student_id = int(input("Enter student ID to delete: "))
            except ValueError:
                print("Invalid ID.")
                continue
            delete_student(students, student_id)
        elif option == 6:
            try:
                student_id = int(input("Enter student ID to calculate average marks: "))
            except ValueError:
                print("Invalid ID.")
                continue
            calculate_average_marks(students, student_id)
        elif option == 7:
            find_highest_scorer(students)
        elif option == 8:
            total_students(students)
        elif option == 9:
            grade_evaluation(students)
        elif option == 0:
            print("Exiting the Student Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid number from 1 to 9.")

def save_students(students):
    with open("Students.json", "w") as f:
        json.dump(students, f, indent=4)
        print("Students saved successfully.")

def load_students():
    try:
        with open("Students.json", "r") as f:
           students = json.load(f)
        if not students:
            print("No students found. Starting with an empty list.")
            return {}
        else:
            print(f"Loaded {len(students)} student(s).")
            return students
    except FileNotFoundError:
        print("No existing student data found.")
        return {}
    except json.JSONDecodeError:
        print("Invalid JSON file.")
        return {}


def add_student(students):
    try:
        student_id = int(input("Enter student ID: "))
        if student_id in students:
            print("Student ID already exists. Please use a different ID.")
            return
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        marks = {}
        marks["Math"] = int(input("Enter Math marks: "))
        marks["Science"] = int(input("Enter Science marks: "))
        marks["English"] = int(input("Enter English marks: "))
        students[student_id] = {
            "name": name,
            "age": age,
            "marks": marks
        }
        save_students(students)
        print(f"Student {name} added successfully.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def view_students(students):
    if not students:
        print("No students found.")
        return
    for student_id, details in students.items():
        print("-" * 30)
        print(f"Student ID : {student_id}")
        print(f"Name       : {details['name']}")
        print(f"Age        : {details['age']}")
        print(f"Math       : {details['marks']['Math']}")
        print(f"Science    : {details['marks']['Science']}")
        print(f"English    : {details['marks']['English']}")
        print("-" * 30)

def search_student(students, student_id):
    if student_id in students:
        details = students[student_id]
        print("-" * 30)
        print(f"Student ID : {student_id}")
        print(f"Name       : {details['name']}")
        print(f"Age        : {details['age']}")
        print(f"Math       : {details['marks']['Math']}")
        print(f"Science    : {details['marks']['Science']}")
        print(f"English    : {details['marks']['English']}")
        print("-" * 30)
    else:
        print("Student not found.")

def update_student(students, student_id):
    if student_id in students:
        name = input("Enter new name (leave blank to keep current): ")
        age = input("Enter new age (leave blank to keep current): ")
        math_marks = input("Enter new Math marks (leave blank to keep current): ")
        science_marks = input("Enter new Science marks (leave blank to keep current): ")
        english_marks = input("Enter new English marks (leave blank to keep current): ")
        if name:
            students[student_id]["name"] = name
        if age:
            students[student_id]["age"] = int(age)
        if math_marks:
            students[student_id]["marks"]["Math"] = int(math_marks)
        if science_marks:
            students[student_id]["marks"]["Science"] = int(science_marks)
        if english_marks:
            students[student_id]["marks"]["English"] = int(english_marks)

        save_students(students)
        print(f"Student ID {student_id} updated successfully.")
    else:
        print("Student not found.")

def delete_student(students, student_id):
    if student_id in students:
        del students[student_id]
        save_students(students)
        print(f"Student ID {student_id} deleted successfully.")
    else:
        print("Student not found.")
    
def calculate_average_marks(students, student_id):
    if student_id in students:
        marks = students[student_id]["marks"]
        average = sum(marks.values()) / len(marks)
        print(f"Average marks for student ID {student_id} is: {average:.2f}")
    else:
        print("Student not found.")

def find_highest_scorer(students):
    highest_average = -1
    top_student_id = None
    for student_id in students:
        average = sum(students[student_id]["marks"].values()) / len(students[student_id]["marks"])
        if average > highest_average:
            highest_average = average
            top_student_id = student_id

    if top_student_id is not None:
        print(f"Name of the highest scorer: {students[top_student_id]['name']}")
        print(f"Age of the highest scorer: {students[top_student_id]['age']}")
        print(f"Average marks: {highest_average:.2f}")
    else:
        print("No students found.")

def total_students(students):
    count = len(students)
    print(f"Total number of students: {count}")

def grade_evaluation(students):
    average_marks = {}
    for student_id, details in students.items():
        average = sum(details["marks"].values()) / len(details["marks"])
        average_marks[student_id] = average
    for student_id, average in average_marks.items():
        if average > 90:
            print(f"Student ID {student_id} Grade: A")
        elif 80 < average <= 90:
            print(f"Student ID {student_id} Grade: B")
        elif 70 < average <= 80:
            print(f"Student ID {student_id} Grade: C")
        elif 60 < average <= 70:
            print(f"Student ID {student_id} Grade: D")
        else:
            print(f"Student ID {student_id} Grade: F")

if __name__ == "__main__":
    main()

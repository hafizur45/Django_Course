import json

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        if subject in self.courses:
            self.grades[subject] = grade
            print(f"Grade {grade} added for {self.name} in {subject}.")
        else:
            print(f"Error: {self.name} is not enrolled in {subject}.")

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} (ID: {self.student_id}) enrolled in {course}.")
        else:
            print(f"{self.name} is already enrolled in {course}.")

    def display_student_info(self):
        self.display_person_info()
        print(f"ID: {self.student_id}")
        print(f"Enrolled Courses: {', '.join(self.courses) if self.courses else 'None'}")
        print(f"Grades: {self.grades}")

class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Student {student.name} (ID: {student.student_id}) added to {self.course_name}.")
        else:
            print(f"Student {student.name} is already enrolled in {self.course_name}.")

    def display_course_info(self):
        print(f"Course Name: {self.course_name}")
        print(f"Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        print("Enrolled Students:", ", ".join([student.name for student in self.students]))

# Data storage
students = {}
courses = {}

# Helper functions for saving/loading data
def save_data():
    data = {
        "students": {s_id: {"name": s.name, "age": s.age, "address": s.address, "id": s.student_id, "grades": s.grades, "courses": s.courses} for s_id, s in students.items()},
        "courses": {c_code: {"name": c.course_name, "code": c.course_code, "instructor": c.instructor, "students": [s.student_id for s in c.students]} for c_code, c in courses.items()}
    }
    with open("student_management_data.json", "w") as f:
        json.dump(data, f)
    print("All student and course data saved successfully.")

def load_data():
    try:
        with open("student_management_data.json", "r") as f:
            data = json.load(f)
            students.clear()
            courses.clear()
            for s_id, s_data in data["students"].items():
                student = Student(s_data["name"], s_data["age"], s_data["address"], s_data["id"])
                student.courses = s_data["courses"]
                student.grades = s_data["grades"]
                students[s_id] = student
            for c_code, c_data in data["courses"].items():
                course = Course(c_data["name"], c_data["code"], c_data["instructor"])
                course.students = [students[s_id] for s_id in c_data["students"]]
                courses[c_code] = course
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No data file found. Starting fresh.")

# Main menu
def main_menu():
    while True:
        print("\n==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")
        choice = input("Select Option: ")

        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            address = input("Enter Address: ")
            student_id = input("Enter Student ID: ")
            students[student_id] = Student(name, age, address, student_id)
            print(f"Student {name} (ID: {student_id}) added successfully.")
        
        elif choice == "2":
            course_name = input("Enter Course Name: ")
            course_code = input("Enter Course Code: ")
            instructor = input("Enter Instructor Name: ")
            courses[course_code] = Course(course_name, course_code, instructor)
            print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

        elif choice == "3":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            if student_id in students and course_code in courses:
                student = students[student_id]
                course = courses[course_code]
                student.enroll_course(course_code)
                course.add_student(student)
            else:
                print("Invalid Student ID or Course Code.")

        elif choice == "4":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            grade = input("Enter Grade: ")
            if student_id in students and course_code in courses:
                student = students[student_id]
                if course_code in student.courses:
                    student.add_grade(course_code, grade)
                else:
                    print("Error: Student not enrolled in the specified course.")
            else:
                print("Invalid Student ID or Course Code.")

        elif choice == "5":
            student_id = input("Enter Student ID: ")
            if student_id in students:
                students[student_id].display_student_info()
            else:
                print("Invalid Student ID.")

        elif choice == "6":
            course_code = input("Enter Course Code: ")
            if course_code in courses:
                courses[course_code].display_course_info()
            else:
                print("Invalid Course Code.")

        elif choice == "7":
            save_data()

        elif choice == "8":
            load_data()

        elif choice == "0":
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

# Run the menu
if __name__ == "__main__":
    main_menu()

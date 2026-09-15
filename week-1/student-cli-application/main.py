import json

class Student:
    def __init__ (self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
# student1 = Student("Ashok", 20, [80, 90, 65])
# student2 = Student("Ravi", 22, [75, 85, 95])

# students = [student1, student2]

def view_students(students):
    if not students:
        print("No students found.")
        return  
    for student in students:
        print(f"Name: {student.name}, Age: {student.age}, Grades: {student.grades}")
    
  
def add_student(students):
    name = input("Enter student name: ")
    if not name:
        print("Name cannot be empty. Please enter a valid name.")
        return
    
    try:
        age = int(input("Enter student age: "))
        if age <= 0:
            raise ValueError("Age must be a positive integer.")
    except ValueError:
        print("Invalid age. Please enter a valid integer.")
        return
    
    try:
        grades_input = input("Enter student grades (comma-separated): ")
        grades = [int(grade.strip()) for grade in grades_input.split(',')]
    except ValueError:
        print("Invalid grades. Please enter valid integers separated by commas.")
        return
    
    new_student = Student(name, age, grades)
    students.append(new_student)
    print(f"Student added: {new_student.name}")
    save_students(students)

def search_student(students):
    name = input("Enter student name to search: ").lower()
    for student in students:
        if student.name.lower() == name:
            print(f"Student found: Name: {student.name}, Age: {student.age}, Grades: {student.grades}")
            return
    
    print("Student not found.")

def delete_student(students):
    name = input("Enter student name to delete: ").lower()
    for student in students:
        if student.name.lower() == name:
            students.remove(student)
            print(f"Student deleted: {student.name}")
            return
    save_students(students)
    print("Student not found.")

students = []

def save_students(students):
    data = []
    
    for student in students:
        student_data = {
            'name': student.name,
            'age': student.age,
            'grades': student.grades
        }
        data.append(student_data)
    
    with open('students.json', 'w') as file:
        json.dump(data, file)
    
    print("Data saved to json successfully. ")
    
def load_students():
    try:
        with open('students.json', "r") as file:
            data = json.load(file)
            students = []
            for student_data in data:
                student = Student(student_data['name'], student_data['age'], student_data['grades'])
                students.append(student)
            return students
    
    except FileNotFoundError:
        print("No data found. Start to enter student data. ")
        return []
    
    
def menu():
    print("\nStudent Management System")
    print("1. Add Students") 
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    
    
def main():
    students = load_students()
    
    while True:
        menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
    
    
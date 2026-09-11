class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


class GraduateStudent(Student):
    def __init__(self, name, grades, research_topic):
        super().__init__(name, grades)
        self.research_topic = research_topic

    def research_area(self):
        return f"Research topic: {self.research_topic}"
    
ram = Student("Ram", [85, 90, 78, 92])
print(f"Student Name: {ram.name}")
print(f"Average Grade: {ram.average_grade()}")

graduate = GraduateStudent("Sanket", [88, 91, 95], "Deepfake Detection")
print(f"Graduate Student: {graduate.name}")
print(f"Average Grade: {graduate.average_grade()}")
print(graduate.research_area())

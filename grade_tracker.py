class Student:
    def __init__(self, name):
        if not name:
            raise ValueError("name is empty")
        self.name = name
        self.grade_course = {}

    def add_grade(self, course, grade):
        self.grade_course[course] = grade

    def __str__(self):
        return f"Student Name: {self.name} \n Grades: {self.grade_course}"


if __name__ == "__main__":
    student = Student("Tony Stark")
    student.add_grade("Math", "85")
    student.add_grade("English", "75")
    print(student)

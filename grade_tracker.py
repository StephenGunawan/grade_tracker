class Student:
    def __init__(self, name):
        if not name:
            raise ValueError("name is empty")
        self.name = name
        self.grade_course = {}

    def add_grade(self, course, grade):
        self.grade_course[course] = grade


if __name__ == "__main__":
    student = Student("Tony Stark")
    print(student.name)

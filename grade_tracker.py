class Student:
    def __init__(self, name):
        if not name:
            raise ValueError("name is empty")
        self.name = name
        self.grade_course = {}


if __name__ == "__main__":
    student = Student("Tony Stark")
    print(student.name)

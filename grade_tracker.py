class Student:
    def __init__(self, name):
        if not name:
            raise ValueError("name is empty")
        self.name = name
        self.grade_course = {}

    def add_grade(self, course, grade):
        if grade < 0 or grade > 100:
            raise InvalidGrade(grade)
        course_key = course.lower()
        self.grade_course.setdefault(course_key, []).append(grade)

    def __str__(self):
        return f"Student Name: {self.name} \n Grades: {self.grade_course}"


class InvalidGrade(Exception):
    def __init__(self, grade, msg="grade must be between 0 to 100 inclusive"):
        self.grade = grade
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f"{self.grade} {self.msg}"


if __name__ == "__main__":
    student = Student("Tony Stark")
    student.add_grade("Math", 85)
    student.add_grade("math", 90)
    student.add_grade("English", 75)
    student.add_grade("History", 100)
    print(student)

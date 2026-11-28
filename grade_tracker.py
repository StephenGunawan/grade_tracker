class Student:
    def __init__(self, name):
        if not name:
            raise ValueError("student name is empty")
        self.name = name
        self.grade_course = {}

    def add_grade(self, course, grade):
        if grade < 0 or grade > 100:
            raise InvalidGrade(grade)
        course_key = course.lower()
        self.grade_course.setdefault(course_key, []).append(grade)

    def course_average(self, course):
        course_key = course.lower()
        total_grade = 0
        for num in self.grade_course[course_key]:
            total_grade += num
        return f" {self.name} [{course_key}] average grade: {letter_grade(total_grade / len(self.grade_course[course_key]))} [{total_grade / len(self.grade_course[course_key])}]"

    def overall_average(self):
        grade_count = 0
        total_grade = 0
        for course in self.grade_course:
            for grade in self.grade_course[course]:
                total_grade += grade
                grade_count += 1
        return total_grade / grade_count

    def __str__(self):
        return f"Student Name: {self.name} \n Grades: {self.grade_course}"


class Course:
    def __init__(self, name):
        if not name:
            raise ValueError("course name is empty")
        self.name = name.lower()
        self.students = []

    def enroll(self, student):
        if not student or not isinstance(student, Student):
            raise InvalidEnrollment(student, "enrollment need a student")

        for person in self.students:
            if student.name == person.name:
                raise InvalidEnrollment(student)
        self.students.append(student)


class InvalidGrade(Exception):
    def __init__(self, grade, msg="grade must be between 0 to 100 inclusive"):
        self.grade = grade
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f"{self.grade} {self.msg}"


class InvalidEnrollment(Exception):
    def __init__(self, student, msg="student enrollement is invalid"):
        self.student = student
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f"{self.student} {self.msg}"


def letter_grade(average):
    if average < 60:
        return "F"
    elif average < 70:
        return "D"
    elif average < 80:
        return "C"
    elif average < 90:
        return "B"
    elif average <= 100:
        return "A"


if __name__ == "__main__":
    student = Student("Tony Stark")
    student.add_grade("Math", 85)
    student.add_grade("math", 90)
    student.add_grade("English", 75)
    student.add_grade("History", 100)
    print(student)
    print(student.course_average("Math"))
    print(student.overall_average())

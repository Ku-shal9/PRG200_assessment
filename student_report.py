# Student Report Card


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        average_mark = sum(self.marks) / len(self.marks)
        return average_mark

    def grade(self):
        avg = self.average()

        if avg >= 80:
            return "A"
        elif avg >= 65:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        avg = self.average()
        grade = self.grade()
        status = ""

        if avg >= 40:
            status = "Pass"
        else:
            status = "Fail"

        print(f"""
        Name: {self.name}
        Average: {avg}
        Grade: {grade}
        Status: {status}
              """)


students = [
    ("Aarav", [78, 85, 60, 90, 72]),
    ("Sita", [45, 50, 38, 60, 55]),
    ("Bishal", [30, 25, 40, 35, 28]),
    ("Priya", [90, 88, 95, 92, 87]),
]

student_report = []

for name, marks in students:
    student_report.append(Student(name, marks))

for student in student_report:
    student.display()

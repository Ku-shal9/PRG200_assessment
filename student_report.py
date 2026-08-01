# Student Report Card

# student class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # calculate average marks
    def average(self):
        average_mark = sum(self.marks) / len(self.marks)
        return average_mark

    # calculate grade based on average marks
    def grade(self):
        avg = self.average()
        # various condition for grading
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

    # function to display grades
    def display(self):
        avg = self.average()
        grade = self.grade()
        status = ""
        # pass/ fail status based on average marks
        if avg >= 40:
            status = "Pass"
        else:
            status = "Fail"
        # printing student report card
        print(f"""
        Name: {self.name}
        Average: {avg}
        Grade: {grade}
        Status: {status}
              """)


# provided data
students = [
    ("Aarav", [78, 85, 60, 90, 72]),
    ("Sita", [45, 50, 38, 60, 55]),
    ("Bishal", [30, 25, 40, 35, 28]),
    ("Priya", [90, 88, 95, 92, 87]),
]
# list of student report cards object
student_report = []
# going through the lis
for name, marks in students:
    # creating student object and appending to the list
    student_report.append(Student(name, marks))
# displaying student report cards
for student in student_report:
    student.display()

# Exam Scheduler (datetime module)
import datetime

# global variable
college_name = "Bhaktapur Multiple Campus"

# provided data
start_date = "2025-05-01"

exams = [
    ("Python Programming", 0),
    ("Data Structures", 3),
    ("Database Systems", 6),
    ("Computer Networks", 10),
    ("Mathematics", 14),
]


# function to parse the date
def parse_date(date_str):
    # datetime module doesn't have strptime method
    # datetime class has strptime
    # so we do datetime.datetime to access the datetime class
    # Y = 4-digit year, m = 2 digit month, d = 2 digit day of month
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return date


# adding days to exam to calculate subject-wise date
def get_exam_date(start_str, days):
    # parsing the date
    exam_starts_in = parse_date(start_str)
    # adding the days by timedelta method
    adding_date_to_exam = exam_starts_in + datetime.timedelta(days=days)
    # formatting date object calculated above
    # strftime formats date objects
    exam_date = adding_date_to_exam.strftime("%Y-%m-%d")
    return exam_date


# printing the actual object
def print_schedule(start_str, exams):
    # printing the global variable
    print(college_name)
    print("Examination Schedule")
    # going through the list of tuples
    for subject, days in exams:
        print(f"{subject}: {get_exam_date(start_str, days)}")


# calling the function
print_schedule(start_date, exams)

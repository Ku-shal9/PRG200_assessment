# average score


def average_score(*marks):
    for mark in marks:
        sum_marks = sum(marks)
        average = sum_marks / len(marks)
    return average


print("Average score:", average_score(85, 90, 78, 92, 88))

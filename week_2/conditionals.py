marks = []
names = []

for i in range(1, 3):
    name = input(f"Enter name of student {i}: ")
    names.append(name)
    n = int(input(f"Enter mark of student {i}: "))
    marks.append(n)


for i in range(len(marks)):
    if marks[i] >= 95:
        print(f"Student {names[i]}: Distinction")
    elif marks[i] >= 80:
        print(f"Student {names[i]}: First Division")
    elif marks[i] >= 65:
        print(f"Student {names[i]}: Second Division")
    elif marks[i] >= 50:
        print(f"Student {names[i]}: Third Division")
    else:
        print(f"Student {names[i]}: Fail")


# for mark in marks:
#     if mark >= 95:
#         print(f"Student {names[marks.index(mark)]}: Distinction")
#     elif mark >= 80:
#         print(f"Student {names[marks.index(mark)]}: First Division")
#     elif mark >= 65:
#         print(f"Student {names[marks.index(mark)]}: Second Division")
#     elif mark >= 50:
#         print(f"Student {names[marks.index(mark)]}: Third Division")
#     else:
#         print(f"Student {names[marks.index(mark)]}: Fail")

# BMI for a Community Health Camp

weight = float(input("Enter weight in kgs: "))
height = float(input("Enter height in cms: "))

height_metres = height / 100

bmi = weight / (height_metres ** 2)

print(f"BMI Index: {bmi:.1f}")


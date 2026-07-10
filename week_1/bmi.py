# BMI for a Community Health Camp

# taking weight and height as input
weight = float(input("Enter weight in kgs: "))
height = float(input("Enter height in cms: "))

# converting the height from cms to metres
height_metres = height / 100

# BMI = weight (in kg) / (height (in m))^2
bmi = weight / (height_metres**2)

# calculate the BMI
print(f"BMI Index: {bmi:.1f}")

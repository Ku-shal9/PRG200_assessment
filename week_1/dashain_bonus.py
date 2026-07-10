# Dashain Bonus Calculator

# taking salary as the input
salary = float(input("Enter monthly basic salary: "))

bonus = salary  # one month's salary is the bonus

# income related deduction
deduction_rate = 0.05

# calculating the deduction amount
deduction = bonus * deduction_rate

# actual bonus after deduction
take_home_bonus = bonus - deduction

# printing the take home bonus
print(f"Take home bonus: {take_home_bonus}")

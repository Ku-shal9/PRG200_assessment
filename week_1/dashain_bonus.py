# Dashain Bonus Calculator

salary = float(input("Enter monthly basic salary: "))

bonus = salary # one month's salary is the bonus

deduction_rate = 0.05

deduction = bonus * deduction_rate

take_home_bonus = bonus - deduction

print(f"Take home bonus: {take_home_bonus}")



# Trekking Permit Cost Calculator

person_1 = float(input("Enter First person's contribution amount: "))
person_2 = float(input("Enter Second person's contribution amount: "))

group_expense = person_1 + person_2

service_charge = group_expense * 0.05

total_cost = group_expense + service_charge

avg_cost = total_cost/2

print(f"Total cost of the group: {total_cost}")
print(f"Average cost of the group: {avg_cost}")



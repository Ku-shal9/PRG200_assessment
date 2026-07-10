# Trekking Permit Cost Calculator

# taking the number of people as input
n = int(input("Enter number of people in the group: "))

contributions = []  # list to store contibution amount of each person

# loop to take contibutions from each person
for i in range(n):
    contribution = float(input(f"Enter person {i + 1}'s TIMS + ACAP fees: "))
    contributions.append(contribution)

# calculating the group expense
group_expense = sum(contributions)

# calculating the service charge
service_charge = group_expense * 0.05

# expense including the charge
total_cost = group_expense + service_charge

# average cost per person incldung the charge
avg_cost = total_cost / n

# prining the results
print(f"Group expense: {group_expense}")
print(f"Total cost of the group: {total_cost}")
print(f"Average cost of the group: {avg_cost}")

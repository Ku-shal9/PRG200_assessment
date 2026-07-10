# Momo Shop Profit Tracker

# take cost price, selling price, and nom of plates sold as input
cost_price = float(input("Enter the cost per plate: "))
sell_price = float(input("Enter the selling per plate: "))
n = float(input("Enter the no. of plates sold: "))

# calculate total revenue
total_revenue = sell_price * n

# calculate the total cost in making the plate
total_cost = cost_price * n

# calculate the total profit
total_profit = total_revenue - total_cost

# calculate the profit margin
profit_margin = (total_profit / total_revenue) * 100

# print the results
print(f"Total Revenue: {total_revenue}")
print(f"Total Cost: {total_cost}")
print(f"Total Profit: {total_profit}")
print(f"Profit Margin: {profit_margin}%")

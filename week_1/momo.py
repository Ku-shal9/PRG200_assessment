# Momo Shop Profit Tracker

cost_price = float(input("Enter the cost per plate: "))
sell_price = float(input("Enter the selling per plate: "))
n = float(input("Enter the no. of plates sold: "))

total_revenue = sell_price*n
total_cost = cost_price*n
total_profit = total_revenue-total_cost
profit_margin = (total_profit/total_revenue)*100

print(f"Total Revenue: {total_revenue}")
print(f"Total Cost: {total_cost}")
print(f"Total Profit: {total_profit}")
print(f"Profit Margin: {profit_margin}%")


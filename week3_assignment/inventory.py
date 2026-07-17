# Inventory Restock Alert

#  inveentory list from the question
inventory = [
    {"item": "Rice", "stock": 5, "threshold": 10},
    {"item": "Eggs", "stock": 24, "threshold": 12},
    {"item": "Milk", "stock": 3, "threshold": 6},
    {"item": "Bread", "stock": 8, "threshold": 5},
    {"item": "Chicken", "stock": 0, "threshold": 4},
    {"item": "Cooking Oil", "stock": 2, "threshold": 3},
]

flag = 0  # counter for items below threshold

for items in inventory:  # looping through the inventory list
    # checking if the stock is below the threshold
    if items["stock"] < items["threshold"]:
        # incrementing the flag counter
        flag += 1
        print(f"Restock Alert: {items['item']} is below threshold.")

print(f"Total number of items to restock: {flag}")

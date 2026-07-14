# Sorting Food Delivery Orders

orders = [
    ("ORD001", "00:03:15"),
    ("ORD002", "00:05:30"),
    ("ORD003", "00:02:45"),
]

orders.sort(key=lambda order: order[1])  # Sort by the second element (time)
for order in orders:
    print(f"Order ID: {order[0]}, Time: {order[1]}")

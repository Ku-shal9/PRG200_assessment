# importing methods from shopping_discount
from shopping_discount import final_price, TAX_RATE

# provided input
products = [
    ("Laptop", 85000, 10),
    ("Headphones", 4500, 15),
    ("Phone Case", 800, 5),
    ("USB Cable", 600, 0),
]
# we can use the global constant that we have imported
print(f"Tax Rate: {TAX_RATE}")

print("\nProduct Details")

# printing the details
for product, price, discount in products:
    print(f"Product: {product}")
    print(f"Original Price: NPR {price}")
    print(f"Final Price: NPR {final_price(price, discount):.2f}")
    print()

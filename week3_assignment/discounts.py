# Online Store Discount System

total_purchase = float(input("Enter the total purchase amount: "))

if total_purchase < 1000:
    discount = 0
    print("No discount available")
elif total_purchase >= 1000 and total_purchase <= 4999:
    discount = total_purchase * 0.05  # Apply 5% discount
elif total_purchase >= 5000 and total_purchase <= 14999:
    discount = total_purchase * 0.1  # Apply 10% discount
elif total_purchase >= 15000:
    discount = total_purchase * 0.2  # Apply 20% discount

loyalty_member = input("Are you a loyalty member? (yes/no): ").strip().lower()

discounted_amount = total_purchase - discount

if loyalty_member == "yes":
    discount += discounted_amount * 0.05  # Additional 5% discount for loyalty members

total_payable = total_purchase - discount
print(f"Discount applied: {discount}")
print(f"Total amount payable: {total_payable}")

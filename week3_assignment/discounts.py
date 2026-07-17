# Online Store Discount System

# total purchase by customer
total_purchase = float(input("Enter the total purchase amount: "))

# condition 1: if the purchase is less than 1000
if total_purchase < 1000:
    discount = 0
    print("Sad! No discount available")

#  condition 2: if the purchase is between 1000 and 4999
elif total_purchase >= 1000 and total_purchase <= 4999:
    print("Quack! 5% discount")
    discount = total_purchase * 0.05  # Apply 5% discount

#  condition 3: if the purchase is between 5000 and 14999
elif total_purchase >= 5000 and total_purchase <= 14999:
    print("Quack! 10% discount")
    discount = total_purchase * 0.1  # Apply 10% discount

#  condition 4: if the purchase is 15000 or more
elif total_purchase >= 15000:
    print("Quack! 20% discount")
    discount = total_purchase * 0.2  # Apply 20% discount

#  checking if the customer is a loyalty member
loyalty_member = input("Are you a loyalty member? (yes/no): ").strip().lower()

discounted_amount = total_purchase - discount  # discounted amount

# additional discount for loyalty members
if loyalty_member == "yes":
    discount += discounted_amount * 0.05  # Additional 5% discount for loyalty members

# bill after discounts
total_payable = total_purchase - discount
print(f"Discount applied: {discount}")
print(f"Total amount payable: {total_payable}")

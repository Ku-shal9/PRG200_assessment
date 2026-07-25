# Small Shop Billing and Inventory System

# input from the question
inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30},
}

cart = {"rice": 2, "milk": 3, "eggs": 12}


def process_order(inventory, cart):  # function to automate inventory process
    tota_bill = 0

    print("\n--- Bill ---\n")

    for item in cart:  # going through all the items in the cart
        # stocks should be available enough
        if cart[item] <= inventory[item]["stock"]:
            # calculating cost
            cost = inventory[item]["price"] * cart[item]

            print(f"{item} ×{cart[item]}: NPR {cost}")

            tota_bill += cost

            inventory[item]["stock"] -= cart[item]  # updating the inventory
        else:
            print(f"Not enough stock for {item}")

    # printing message
    print(f"Grand Total: {tota_bill}\n")
    print("--- Updated Inventory --- \n")
    # updated inventory
    for item in inventory:
        print(f"{item}: updated_stock: {inventory[item]['stock']}")


process_order(inventory, cart)  # calling the function

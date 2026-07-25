#  Simple ATM Simulator
accounts = {
    "A001": {"name": "Ramesh Thapa", "balance": 15000, "pin": "1234"},
    "A002": {"name": "Sunita Karki", "balance": 8500, "pin": "5678"},
    "A003": {"name": "Bikash Rai", "balance": 22000, "pin": "9012"},
}


# function to simulate ATM
def atm(account_id, pin, action, amount=0):
    # looping through the dictionary
    if account_id not in accounts:  # checking if the account exists
        print("Account not found")
        return
    # checking the correctness of pin
    if accounts[account_id]["pin"] != pin:
        print("incorrect PIN")
        return
    # pulling profile details
    if action == "balance":
        print(
            f"Name: {accounts[account_id]['name']} | Balance: {accounts[account_id]['balance']}"
        )
    # depositing the money
    elif action == "deposit":
        accounts[account_id]["balance"] += amount
        print("Deposit success!")
        print(f"New Balance: {accounts[account_id]['balance']}")
    # withdrawing the money
    elif action == "withdraw":
        if amount > accounts[account_id]["balance"]:
            print("Insufficient Balance")
        else:
            accounts[account_id]["balance"] -= amount
            print("Withdrawal success!")
            print(f"New Balance: {accounts[account_id]['balance']}")


# calling the function
atm("A001", "1234", "balance")
atm("A002", "0000", "withdraw", 2000)
atm("A002", "5678", "deposit", 3000)
atm("A003", "9012", "withdraw", 25000)
atm("A004", "1111", "balance")

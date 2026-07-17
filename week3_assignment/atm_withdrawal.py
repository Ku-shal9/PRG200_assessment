# ATM Withdrawal Validator

# taking input from the user
curr_balance = int(input("Enter your current balance: "))
daily_withdrawn = int(input("Enter the total amount already withdrawn today: "))
amount = int(input("Enter the amount you want to withdraw: "))

# condition 1: withdrawal amount must be a multiple of 500
if amount % 500 != 0:
    print("Withdrawal amount must be a multiple of 500")

# condition 2: withdrawal amount must not exceed current balance
elif amount > curr_balance:
    print("Withdrawal amount exceeds current balance")

# condition 3: daily withdrawal limit must not be exceeded
elif daily_withdrawn + amount > 50000:
    print("Daily withdrawal limit exceeded")

# if all conddiitions are passed then proceed with withdrawal
else:
    curr_balance -= amount
    print("Withdrawal successful!")
    print(f"Your current balance after withdrawal is: {curr_balance}")

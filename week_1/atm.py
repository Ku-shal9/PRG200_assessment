# classwork: simulate ATM machine

pin_user = 9999  # hardooding the pin
flag = 0  # user trials

username = input("Enter the username: ")  # username input

# user has only three attempts to enter the correct pin in total
for i in range(3):
    # taking pin as the input
    pin_input = int(input("Enter the pin: "))

    # checking the correctness of the pin
    if pin_input == pin_user:
        # user is able to take amount once they enter correct pin
        amount = float(input("Enter the amount to withdraw: "))
        print(f"Withdrawing {amount} from your account.")
        # user attempt is successful
        flag += 1
        break
    else:
        # user attempt is unsuccessful
        print("pin verification failed, try again")

if flag == 0:
    # if user fails to enter the correct pin in 3 attempts
    print("Pin didn't match for 3 attempts")

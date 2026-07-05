pin_user = 9999
flag = 0

username = input("Enter the username: ")

for i in range(3):
    pin_input = int(input("Enter the pin: "))
    
    if(pin_input==pin_user):
        print("Enter the amount")
        flag += 1
        break
    else:
        print("pin verification failed, try again")

if(flag == 0):
    print("Pin didn't match for 3 attempts")


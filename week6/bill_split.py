#  Bill Splitter (random module)
import random  # generates a random number

random.seed(42)  # consistency in randomness


# split bill function to split the bill equally among friends
def split_bill(friends, total):
    amount = total / len(friends)
    return amount


# selecting the random person
def pick_lucky(friends):
    return random.choice(friends)


# printing the final summary
def final_summary(friends, total):
    # local variables for getting info on lucky person
    lucky_person = pick_lucky(friends)
    pay = split_bill(friends, total)

    print("Each Person's Share")
    # going through the friend's list
    for i in range(len(friends)):
        # skipping the lucky person as they are lucky :)
        # skipping as it is redundant and may create confusion
        if friends[i] == lucky_person:
            pass  # just skips
        else:
            # printing everyone's share
            print(f"{friends[i]}: NPR {pay}")
    print(" ")
    # lucky person pays NPR 50 extra
    lucky_total = pay + 50
    print("Lucky Person Total")
    print(f"{lucky_person}: NPR {lucky_total}")


# provided input
friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]
total_bill = 3750
# calling the function
final_summary(friends, total_bill)

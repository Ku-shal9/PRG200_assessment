# Password Strength Checker

# password list from the question
passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]

# list of special character
special_characters = "!@#$%^&*"

# looping through all the passwords
for password in passwords:
    strength = 0  # assigning strengths to passwords

    print(f"Checking the Password: {password}")

    missing_criteria = []  # list of feedbacks

    if len(password) >= 8:  # condition 1: 8 characters of length
        strength += 1  # strength up
    else:
        missing_criteria.append(
            "Insufficient length"
        )  # add feedback to missing criteria list

    # boolean variables for other conditions
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:  # looping through all the characters of a password
        # condition 2: checking the uppercase character
        if char.isupper():
            has_upper = True
            strength += 1
            break  # exit the loop immediately
    if not has_upper:  # if boolean variables is still false
        missing_criteria.append("Missing an uppercase character")

    for char in password:
        # condition 3: checking the lowerecase character
        if char.islower():
            has_lower = True
            strength += 1
            break
    if not has_lower:
        missing_criteria.append("Missing a lowercase character")

    for char in password:
        # condition 4: checking if there are digits
        if char.isdigit():
            has_digit = True
            strength += 1
            break
    if not has_digit:
        missing_criteria.append("Missing a digit")

    for char in password:
        # condition 5: checking special characters
        if char in special_characters:
            has_special = True
            strength += 1
            break
    if not has_special:
        missing_criteria.append("Missing a special character")

    # strength-wise category of password
    if strength == 5:
        print("Strong Password")
    elif strength == 3:
        print("Good password, potential warning")
    else:
        print("Weak Password")

    if missing_criteria:
        for misses in missing_criteria:
            print(misses)
    print(" ")

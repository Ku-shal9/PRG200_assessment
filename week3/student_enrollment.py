# student enrollment profile

name = input("Enter your name: ")
age = input("Enter your age: ")
major = input("Enter your major: ")
email = input("Enter your email: ")


def build_profile(name, **details):
    print(f"Name: {name}")
    for key, value in details.items():
        print(f"{key}: {value}")


build_profile(name, age=age, major=major, email=email)

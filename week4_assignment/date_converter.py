# Date Converter for Nepal Bank System (BS ↔ AD)
bs_months = [
    "Baisakh",
    "Jestha",
    "Ashadh",
    "Shrawan",
    "Bhadra",
    "Ashwin",
    "Kartik",
    "Mangsir",
    "Poush",
    "Magh",
    "Falgun",
    "Chaitra",
]
customers = [
    {
        "name": "Ramesh Thapa",
        "date": "1985-06-24",
        "cal": "AD",
        "need": "BS",
        "style": "full",
    },
    {
        "name": "Sunita Karki",
        "date": "2055-09-10",
        "cal": "BS",
        "need": "AD",
        "style": "iso",
    },
    {
        "name": "Bikash Rai",
        "date": "1998-11-30",
        "cal": "AD",
        "need": "BS",
        "style": "nepali",
    },
    {
        "name": "Anjali Gurung",
        "date": "2040-01-05",
        "cal": "BS",
        "need": "AD",
        "style": "full",
    },
]


# function to convert the date
def convert_date(date_str, from_cal, to_cal):
    # utilizing the split method
    year, month, day = date_str.split("-")
    # print(type(year))  # checking the type of variable as split method returns string type
    # typecasting the data-type of year
    year = int(year)  # explicit conversion to perform mathematical operation
    # condition 1: when the to and from conversion are same
    if from_cal == to_cal:
        return date_str
    # condition2: conversion from AD to BS
    elif from_cal == "AD" and to_cal == "BS":
        year = year + 56
    # condition3: conversion from BS to AD
    elif from_cal == "BS" and to_cal == "AD":
        year = year - 56
    else:
        return "invalid"
    converted_date = f"{year}-{month}-{day}"
    return converted_date


# iterating through the list
for customer in customers:
    # calling the function
    converted = convert_date(customer["date"], customer["cal"], customer["need"])

    year, month, day = converted.split("-")
    # printing in desired format
    if customer["style"] == "iso":
        print(customer["name"], ":", converted)

    elif customer["style"] == "full":
        print(customer["name"], ":", day + "-" + month + "-" + year)

    elif customer["style"] == "nepali":
        # list starts from the index 0
        month_name = bs_months[int(month) - 1]
        print(customer["name"], ":", day, month_name, year)

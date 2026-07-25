# Water Level Alert System (Koshi River)
# sample input
sensors = [
    ("Chatara", 2.8),
    ("Tribeni Ghat", 5.4),
    ("Koshi Barrage", 4.1),
    ("Sunsari Bridge", 1.9),
    ("Saptakoshi Camp", 6.0),
]


# location = first element of tuple
# level_metres = second element of tuple
def check_water_level(location, level_metres):  # function to check water level
    # first condition: water below 3m is safe
    if level_metres < 3:
        return "safe"
    # second condition: water between 3 m and 5 m is a warning
    elif level_metres < 5:
        return "Warning, nearby villagers"
    # third condition: water above 5 m is dangerous
    elif level_metres > 5:
        return "Danger, evacuate immediately"
    else:
        return "invalid input"


# iterating through list of tuples
for location, level_metres in sensors:
    # calling the function
    alert = check_water_level(location, level_metres)
    # printing alerts for all rivers
    print(f"{location} ({level_metres} m): {alert}")

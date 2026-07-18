# Taxi Fare Calculator

# list data from question
trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]

# looping through the trips
for trip in trips:
    # base fare
    if trip["distance"] <= 2:
        fare = 150

    # fare for next 8km is base fare + 35 per km
    elif trip["distance"] <= 10:
        fare = 150 + (trip["distance"] - 2) * 35

    # fare beyond 10km is base fare + fare for 8 km + fare for remaining distance (28 per km)
    elif trip["distance"] > 10:
        fare = 150 + (8 * 35) + (trip["distance"] - 10) * 28
    else:
        print("Enter valid distance")

    # additional 10% for night trip
    if trip["hour"] >= 22 or trip["hour"] < 5:
        fare += fare * 0.1

    print(f"Trip {trip['distance']} KM at Time: {trip['hour']} costs NPR {fare:.2f}")

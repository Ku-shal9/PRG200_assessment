# ride fair estimator

distance_km = float(input("Enter distance in kilometers: "))
vehicle_type = input("Enter vehicle type (standard/premium/luxury): ")


def estimate_fare(distance_km, vehicle_type, surge=1.0):
    base_fares = {
        "standard": 5.0,
        "premium": 10.0,
        "luxury": 20.0,
    }

    fare = base_fares.get(vehicle_type.lower(), 0) * distance_km * surge
    return fare


print(f"Estimated fare: ${estimate_fare(distance_km, vehicle_type):.2f}")

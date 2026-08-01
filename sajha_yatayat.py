class Bus:
    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = []

    def book_seat(self, seat_number, passenger_name):
        for seat, passenger in self.booked:
            if seat == seat_number:
                print("Oops! Seat is not available")
                return

        self.booked.append((seat_number, passenger_name))
        print(f"Seat {seat_number} booked for {passenger_name}")

    def available_seats(self):
        available_seats = self.total_seats - len(self.booked)
        return available_seats

    def passenger_list(self):
        print("\nPassenger List:")

        for seat, passenger in sorted(self.booked):
            print(f"Seat {seat}: {passenger}")


bus = Bus("Kathmandu - Pokhara", 10)

bookings = [
    (3, "Ramila Shrestha"),
    (7, "Deepak Gurung"),
    (3, "Anita Rai"),  # Duplicate
    (1, "Prakash Magar"),
    (7, "Suman Tamang"),  # Duplicate
]

for seat, passenger in bookings:
    bus.book_seat(seat, passenger)

print(f"\nAvailable Seats: {bus.available_seats()}")

bus.passenger_list()

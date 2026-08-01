# Bus Ticket Booking (Sajha Yatayat)
# class of Bus
class Bus:
    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = []  # list for booking status

    # function to book a seat
    def book_seat(self, seat_number, passenger_name):
        # checking if the seat is already booked
        for seat, passenger in self.booked:
            # if the applied seat number and
            # book number in the list is same then seat is not available
            if seat == seat_number:
                print("Oops! Seat is not available")
                return
        # if the seat is available then booking is done
        self.booked.append((seat_number, passenger_name))
        print(f"Seat {seat_number} booked for {passenger_name}")

    # function to check available seats
    def available_seats(self):
        available_seats = self.total_seats - len(self.booked)
        return available_seats

    # function to display passenger list
    def passenger_list(self):
        print("\nPassenger List:")

        for seat, passenger in sorted(self.booked):
            print(f"Seat {seat}: {passenger}")


# provided data
bus = Bus("Kathmandu - Pokhara", 10)

bookings = [
    (3, "Ramila Shrestha"),
    (7, "Deepak Gurung"),
    (3, "Anita Rai"),  # Duplicate
    (1, "Prakash Magar"),
    (7, "Suman Tamang"),  # Duplicate
]
# going through the bookings and booking the seats
for seat, passenger in bookings:
    bus.book_seat(seat, passenger)

print(f"\nAvailable Seats: {bus.available_seats()}")

bus.passenger_list()

# Movie Ticket Price Calculator

seat_type = input("Enter seat type (regular/recliner): ")
count = int(input("Enter number of tickets: "))


def ticket_price(seat_type, count):
    prices = {
        "regular": 10,
        "recliner": 15,
    }

    return prices.get(seat_type, 0) * count


print(ticket_price(seat_type, count))

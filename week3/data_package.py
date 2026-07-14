# NCELL Data Package

gb = input("Enter data package (Sadhain ON/Unlimited 24hr): ")


def recharge_cost(gb):
    prices = {
        "sadhain on": 399,
        "unlimited 24hr": 50,
    }

    return prices.get(gb.lower().strip(), 0)


print(recharge_cost(gb), "Validity: 30 days")

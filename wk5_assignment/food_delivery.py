#  Food Delivery App

# parent class: DeliveryPartner
class DeliveryPartner:
    # constructor to define arguments that all class take
    def __init__(self, name, partner_id, deliveries):
        self.name = name
        self.parent_id = partner_id
        self.deliveries = deliveries

    # function that is inherited by all
    def total_earning(self):
        pass

    # function that displays information
    def display(self):
        print(f"""
        Name: {self.name}
        Deliveries: {self.deliveries}
        Total Earning: Rs. {self.total_earning()}
        """)


# child class: BikeRider
class BikeRider(DeliveryPartner):
    # constructor that defines km_travelled taken by this class
    def __init__(self, name, partner_id, deliveries, km_travelled):
        # super() calls methods from parent class
        super().__init__(name, partner_id, deliveries)
        self.km_travelled = km_travelled

    # now this function is inherited
    # cost for normal delivery
    def total_earning(self):
        total = self.deliveries * 80 + self.km_travelled * 5
        return total


# child class: Walker
class Walker(DeliveryPartner):
    # this child class takes rainy_deliveries as an extra argument
    def __init__(self, name, partner_id, deliveries, rainy_deliveries):
        super().__init__(name, partner_id, deliveries)
        self.rainy_deliveries = rainy_deliveries

    # cost in rainy delivery
    def total_earning(self):
        total = self.deliveries * 60 + self.rainy_deliveries * 50
        return total


# child class: CarDriver
class CarDriver(DeliveryPartner):
    # this child class takes fuel_cost as an extra argument
    def __init__(self, name, partner_id, deliveries, fuel_cost):
        super().__init__(name, partner_id, deliveries)
        self.fuel_cost = fuel_cost

    # cost in car delivery
    def total_earning(self):
        total = self.deliveries * 120 - self.fuel_cost
        return total


# provided data to test
partners = [
    BikeRider("Santosh Rai", "B-01", 15, 42),
    Walker("Kabita Maharjan", "W-01", 18, 5),
    CarDriver("Roshan KC", "C-01", 20, 850),
]
# going through the partners list
for partner in partners:
    # calling the display method
    partner.display()

# NEA Electricity Unit Cost

# taking previous and current meter readings
prev_reading = float(input("Enter the previous meter readings: "))
curr_reading = float(input("Enter the current meter readings: "))

# defining the flat per unit rate and service charge
flat_per_unit_rate = 15
service_charge = 20

# calculating the total bill
total_bill = ((curr_reading - prev_reading) * flat_per_unit_rate) + service_charge

# printing total bill
print(f"Total bill: {total_bill}")

# NEA Electricity Unit Cost

prev_reading = float(input("Enter the previous meter readings: "))
curr_reading = float(input("Enter the current meter readings: "))

flat_per_unit_rate = 15
service_charge = 20

total_bill = ((curr_reading-prev_reading)*flat_per_unit_rate) + service_charge

print(f"Total bill: {total_bill}")


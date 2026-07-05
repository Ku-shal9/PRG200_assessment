# Foreign Remittance Converter

# taking inputs
amount_sent = int(input("Enter the amount you want to send in USD: "))
exchange_rate = float(input("Enter the exchange rate: "))
service_fee_percentage = float(input("Enter the service fees percentage: "))

# calculation
converted_amount = amount_sent*exchange_rate # converting 

added_charge = (service_fee_percentage/100)*converted_amount # fees charged by bank

final_amount = converted_amount-added_charge # final amount received

print(f"Converted Amount: NPR {converted_amount:.2f}")
print(f"Fee Charged (Taken by Bank): NPR {added_charge:.2f}")
print(f"Final amount received: {final_amount:.2f}")
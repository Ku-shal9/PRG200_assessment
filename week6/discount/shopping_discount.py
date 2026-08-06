#  Shopping Discount (own module)

# global constant
TAX_RATE = 0.13


# applying the discount
def apply_discount(price, percent):
    # subtracting discount amount from the price
    return price - (percent / 100) * price


# applying the tax
def apply_tax(price):
    # taxed price is tax amount + discounted price
    return price + (TAX_RATE * price)


# calculating the final price using the above two modules
def final_price(price, discount_pct):
    # apply_discount() returns the discounted amount
    discounted_price = apply_discount(price, discount_pct)
    # this discounted amount is passed into the apply_tax() module
    taxed_amount = apply_tax(discounted_price)
    # return the taxed amount
    return taxed_amount

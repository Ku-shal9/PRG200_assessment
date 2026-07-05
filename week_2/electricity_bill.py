shop_name = []
units_consumed = []

for i in range(1, 3):
    name = input(f"Enter name of shop {i}: ")
    shop_name.append(name)
    n = int(input(f"Enter units consumed by shop {i}: "))
    units_consumed.append(n)

while len(units_consumed) > 0:
    for i in range(len(units_consumed)):
        if units_consumed[i] <= 100:
            print(f"Shop {shop_name[i]}: Bill is {units_consumed[i] * 5}")
        elif units_consumed[i] <= 200:
            print(f"Shop {shop_name[i]}: Bill is {units_consumed[i] * 7}")
        else:
            print(f"Shop {shop_name[i]}: Bill is {units_consumed[i] * 10}")
    break

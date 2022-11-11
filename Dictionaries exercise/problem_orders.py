entry = input()
product_price = {}
product_quantity = {}

while entry != "buy":
    product, price, quantity = entry.split()
    if not product in product_quantity:
        product_quantity[product] = int(quantity)
    else:
        product_quantity[product] += int(quantity)
    product_price[product] = float(price)
    entry = input()
for key, value in product_quantity.items():
    value = product_price[key] * product_quantity[key]
    print(f"{key} -> {value:.2f}")


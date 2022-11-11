def product_calculation(product_type, product_num):
    if product == "coffee":
        return f" {1.5 * product_num:.2f}"
    elif product == "water":
        return f"{1 * product_num:.2f}"
    elif product == "coke":
        return f"{1.4 * product_num:.2f}"
    elif product == "snacks":
        return f"{2 * product_num:.2f}"


product = input()
num_of_products = int(input())
print(product_calculation(product, num_of_products))
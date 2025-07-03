metal = input()
result = {}

while True:

    if metal != 'stop':
        quantity = int(input())
        if metal not in result:
            result[metal] = quantity
        else:
            result[metal] += quantity

        metal = input()
    else:
        break

for key, value in result.items():
    print(f"{key} -> {value}")

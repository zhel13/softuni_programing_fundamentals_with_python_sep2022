parameter = input()
num_1 = int(input())
num_2 = int(input())


def calculations(number_1, number_2):
    if parameter == "multiply":
        return number_1 * number_2
    elif parameter == "divide":
        return number_1 // number_2
    elif parameter == "add":
        return number_1 + number_2
    elif parameter == "subtract":
        return number_1 - number_2


print(calculations(num_1, num_2))
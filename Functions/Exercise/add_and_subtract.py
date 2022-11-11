def sum_numbers(number_1, number_2):
    return number_1 + number_2


def subtract(result_sum, number3):
    return result_sum - number3


def add_and_subtract(number_1, number_2, number_3):
    adding_first_two_numbers = sum_numbers(number_1, number_2)
    subtracting = subtract(adding_first_two_numbers, number_3)
    return subtracting


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
print(add_and_subtract(num_1, num_2, num_3))

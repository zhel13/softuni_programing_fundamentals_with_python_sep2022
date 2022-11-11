def positive(some_number):
    return [number for number in some_number if int(number) >= 0]


def negative(some_number):
    return [number for number in some_number if int(number) < 0]


def even(some_number):
    return [number for number in some_number if int(number) % 2 == 0]


def odd(some_number):
    return [number for number in some_number if int(number) % 2 != 0]


num_entry = input().split(", ")
print(f"Positive: {', '.join(positive(num_entry))}")
print(f"Negative: {', '.join(negative(num_entry))}")
print(f"Even: {', '.join(even(num_entry))}")
print(f"Odd: {', '.join(odd(num_entry))}")

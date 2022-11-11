def perfect_num(some_number):
    sum_numbers = 0
    for num in range(1, number):
        if number % num == 0:
            sum_numbers += num
    if sum_numbers == number:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfect_num(number))

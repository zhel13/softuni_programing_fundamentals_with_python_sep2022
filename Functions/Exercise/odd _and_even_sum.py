def even_odd_sum():

    odd_sum = 0
    even_sum = 0

    for number in single_number:
        new_num = int(number)
        if new_num % 2 == 0:
            even_sum += new_num
        else:
            odd_sum += new_num
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


single_number = input()

even_odd_sum()

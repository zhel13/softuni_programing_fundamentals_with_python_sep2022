num_input = input().split()
num_list = []


def num_conversion():
    for value in num_input:
        num_value = int(value)
        num_list.append(num_value)


b = list(filter(lambda x: x%2 == 0, num_conversion()))


print(num_conversion(b))






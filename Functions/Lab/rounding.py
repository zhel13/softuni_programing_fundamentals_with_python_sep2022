number_string = input().split()
num_list = []


def rounding(a):
    for result in number_string:
        num_list.append(round(float(result)))
    print(num_list)


rounding(num_list)




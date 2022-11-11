number_string = input().split()
inverted_num = []
for numbers in number_string:
    num_inverted = int(numbers) * -1
    inverted_num.append(num_inverted)
print(inverted_num)
num_input = input().split()
list_num = []
for number in range(len(num_input)):
    numbers = float(num_input[number])
    list_num.append(abs(numbers))
print(list_num)




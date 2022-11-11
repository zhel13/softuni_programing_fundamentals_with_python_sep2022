numbers = input().split(", ")
beggers = int(input())
list_sums = []
total_amount_list = []
counter_index = 0
total_amount = 0
for index in range (len(numbers)):
    list_sums.append(int(numbers[index]))
while counter_index < beggers:
    for amount in range(counter_index, len(numbers), beggers):
        total_amount += list_sums[amount]
    total_amount_list.append(total_amount)
    total_amount = 0
    counter_index += 1
print(total_amount_list)































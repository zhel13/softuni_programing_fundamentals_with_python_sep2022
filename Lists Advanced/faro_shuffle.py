card_input = input().split(" ")
faro_shuffle = int(input())
left_half_list = []
right_half_list = []
for left in range(faro_shuffle):
    total_list = []
    half = len(card_input) // 2
    left_half_list = card_input[:half]
    right_half_list = card_input[half:]
    for card in range(half):
        total_list.append(left_half_list[card])
        total_list.append(right_half_list[card])
    card_input = total_list

print(total_list)

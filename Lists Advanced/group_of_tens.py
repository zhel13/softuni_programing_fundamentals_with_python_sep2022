num_list = [int(num) for num in input().split(", ")]
new_list = []
max_num = max(num_list)
group = max_num // 10
if max_num % 10 != 0:
    group = max_num // 10 + 1
for number in range(1, group +1):
    groups = number * 10
    sum_list = sum(num_list)
    for index, digit in enumerate(num_list):
        if digit == 0:
            continue
        elif digit <= groups:
            popped = num_list.pop(index)
            new_list.append(popped)
            num_list.insert(index, 0)

    print(f"Group of {groups}'s: {new_list}")
    new_list.clear()

number = int(input())

for index in range(1, number+1):
    digits = index
    total_sum = 0
    while digits > 0:
        total_sum += digits % 10
        digits = digits // 10
    if total_sum == 5 or total_sum == 7 or total_sum == 11:
        print(f"{index} total sum = {total_sum} -> True")
    else:
        print(f"{index} total sum = {total_sum} -> False")





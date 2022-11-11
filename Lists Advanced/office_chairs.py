number_of_rooms = int(input())
total_empty_chairs = 0
total_needed_chairs = 0
for room in range(1, number_of_rooms+1):
    chairs, visitors = input().split()
    difference = len(chairs) - int(visitors)
    if difference >= 0:
        total_empty_chairs += difference
    else:
        total_needed_chairs += abs(difference)
        print(f"{abs(difference)} more chairs needed in room {room}")
if total_empty_chairs >= total_needed_chairs:
    print(f"Game On, {total_empty_chairs} free chairs left")



# team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# card_input = input().split()
# is_terminated = False
#
# for cards in card_input:
#     card_split = cards.split("-")
#     team_name = card_split[0]
#     player_num = int(card_split[1])
#     if team_name == "A" and player_num in team_A:
#         team_A.remove(player_num)
#     elif team_name == "B" and player_num in team_B:
#         team_B.remove(player_num)
#     if len(team_A) < 7 or len(team_B) < 7:
#         is_terminated = True
#         break
#
# print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
# if is_terminated:
#     print("Game was terminated")

# football cards_v2
team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
game_was_terminated = False
sent_off = input().split(" ")
for player in sent_off:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if int(len(team_a)) < 7 or int(len(team_b)) < 7:
        game_was_terminated = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminated:
    print("Game was terminated")



number = int(input())
is_balanced = True
counter_open_bracket = 0
counter_closing_bracket = 0
for _ in range(number):
    entry = input()
    if entry == ")":
        counter_closing_bracket += 1
    elif entry == "(":
        counter_open_bracket += 1
    elif counter_open_bracket - counter_closing_bracket >= 2:
        is_balanced = False
        break
    if counter_closing_bracket != counter_open_bracket:
        is_balanced = False
    else:
        is_balanced = True
if is_balanced:
    print("BALANCED")
else:
    is_balanced = False
    print("UNBALANCED")


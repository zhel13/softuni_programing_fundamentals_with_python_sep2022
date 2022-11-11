phone_book = {}
while True:
    entry = input()
    if not "-" in entry:
        break
    name, number = entry.split("-")
    phone_book[name] = number
for _ in range(int(entry)):
    searched_name = input()
    if searched_name in phone_book:
        print(f"{searched_name} -> {phone_book[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
commands = int(input())
registered = {}
unregistered = {}
for command in range(commands):
    order = input().split()
    confirmation = order[0]
    name = order[1]
    if confirmation == "register":
        plate_number = order[2]
        if not name in registered:
            registered[name] = plate_number
            print(f"{name} registered {registered[name]} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered[name]}")
    else:
        if name not in registered:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del registered[name]
for key, value in registered.items():
    print(f"{key} => {value}")

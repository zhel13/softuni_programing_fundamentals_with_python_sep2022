wagons_len = int(input())
wagon = wagons_len * [0]
command = input()

while command != "End":
    command_list = command.split()
    key_command = command_list[0]

    if key_command == "add":
        wagon[-1] += int(command_list[1])

    elif key_command == "insert":
        wagon[int(command_list[1])] += int(command_list[2])
    elif key_command == "leave":
        wagon[int(command_list[1])] -= int(command_list[2])
    command = input()
print(wagon)




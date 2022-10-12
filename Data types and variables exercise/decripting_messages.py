key_input = int(input())
letter_input = int(input())
for index in range(letter_input):
    letter = input()
    letter_num = ord(letter)
    new_letter = letter_num + key_input
    print(chr(new_letter), end="")


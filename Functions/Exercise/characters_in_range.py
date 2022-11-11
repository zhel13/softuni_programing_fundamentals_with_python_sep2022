character_1 = input()
character_2 = input()


def char_in_range(chr_1, chr_2):

    for character in range(ord(character_1)+1, ord(character_2)):
        new_char = chr(character)
        print(new_char, end=" ")


char_in_range(character_1, character_2)
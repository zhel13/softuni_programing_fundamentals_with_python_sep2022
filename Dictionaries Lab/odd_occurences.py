words = input().split()
program_dict = {}
for word in words:
    lower_words = word.lower()
    if lower_words not in program_dict:
        program_dict[lower_words] = 0
    program_dict[lower_words] += 1
for key, value in program_dict.items():
    if value % 2 != 0:
        print(key, end=" ")

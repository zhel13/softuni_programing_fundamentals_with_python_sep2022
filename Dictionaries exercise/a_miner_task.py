word = input()
word_list = []
word_dict = {}

while word != "stop":
    word_list.append(word)
    word = input()
for i in range(0, len(word_list), 2):
    key = word_list[i]
    value = word_list[i+1]
    if key not in word_dict.keys():
        word_dict[key] = 0
    word_dict[key] += int(value)

for key, value in word_dict.items():
    print(f"{key} -> {value}")

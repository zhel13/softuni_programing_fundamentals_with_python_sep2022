first_sentence = input().split(", ")
second_sentence = input().split(", ")
result = []
for firs_word in first_sentence:
    for second_word in second_sentence:
        if firs_word in second_word:
            result.append(firs_word)
            break

print(result)
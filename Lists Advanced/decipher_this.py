word_input = input().split()
is_digit = []
no_digit = []

for word in word_input:

    for ch in word:
        if ch.isdigit():
            is_digit.append(ch)
        else:
            no_digit.append(ch)

    no_digit[0], no_digit[-1] = no_digit[-1], no_digit[0]
    digits = "".join(is_digit)
    print(f"{chr(int(digits))}{''.join(no_digit)}", end=" ")
    no_digit.clear()
    is_digit.clear()












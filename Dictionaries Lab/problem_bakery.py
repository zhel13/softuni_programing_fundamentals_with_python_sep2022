elements = input().split()
dictionary_input = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i+1]
    dictionary_input[key] = int(value)
print(dictionary_input)

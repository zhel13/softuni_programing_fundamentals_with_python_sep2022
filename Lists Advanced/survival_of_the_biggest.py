numbers = input().split()
num_to_remove = int(input())
num_list = []
for index in range(len(numbers)):
    num_list.append(int(numbers[index]))
for element in range(num_to_remove):
    min_element = min(num_list)
    num_list.remove(min_element)
for element2 in range(len(num_list)):
    num_list[element2] = str(num_list[element2])
print(", ".join(num_list))



number_of_electrons = int(input())
electron_shell = []
total_shell = 0
for position in range(1, number_of_electrons+1):
    maximum_num_of_electrons = 2 * position**2
    total_shell += maximum_num_of_electrons
    if total_shell < number_of_electrons:
        electron_shell.append(maximum_num_of_electrons)
    else:
        total_shell -= maximum_num_of_electrons
        result = number_of_electrons - total_shell
        electron_shell.append(result)
        break
print(electron_shell)
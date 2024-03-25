def electron_distribution(electron_count):
    electron_shell = 1
    distributed_electrons = list()
    while True:
        current_electron_shell_max = (electron_shell ** 2) * 2
        if electron_count > current_electron_shell_max:
            electron_count -= current_electron_shell_max
            distributed_electrons.append(current_electron_shell_max)
        else:
            distributed_electrons.append(electron_count)
            break
        electron_shell += 1

    return distributed_electrons


electrons_count = int(input())
print(electron_distribution(electrons_count))

def next_version(version):
    version = int(version.replace(".", ""))
    version += 1
    output_version = list()
    [output_version.append(x) for x in str(version)]

    return '.'.join(output_version)


current_version = input()

print(next_version(current_version))

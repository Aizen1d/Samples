def capital_indexes(string):
    indexes = []

    for index, letter in enumerate(string):
        if letter.isupper():
            indexes.append(index)

    return indexes


print(capital_indexes("HeLlO"))


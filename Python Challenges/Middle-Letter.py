def mid(string):
    length = len(string)
    middle = length // 2

    if length % 2 == 0:
        return ""
    else:
        return string[middle]

print(mid("abc"))
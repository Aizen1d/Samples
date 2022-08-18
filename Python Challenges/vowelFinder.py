
inputWord = "Hello there guys"

def findVowels(word):
    total = 0
    a, e, i, o, u = 0, 0, 0, 0, 0

    for letter in word:
        if letter.upper() == "A":
            a = a + 1
        elif letter.upper() == "E":
            e = e + 1
        elif letter.upper() == "I":
            i = i + 1
        elif letter.upper() == "O":
            o = o + 1
        elif letter.upper() == "U":
            u = u + 1

    total = ("Total = " + str((total + a + e + i + o + u)), "A = " + str(a), "E = " + str(e), "I = "
                                        + str(i), "O = " + str(o), "U = " + str(u))

    return total

print(findVowels(inputWord))

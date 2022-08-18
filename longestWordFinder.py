""" Finds the longest word in a sentence [this is a long method] """

yourWord = "hello there guys" # input

def LongestWord(sen):
    inputLetters = [] # Letters from the input
    words = [] # Words container
    punctuations = [".", ",", "?", "!", ":", ";", "'", '"', "&"] # Unallowed characters
    constructWord = "" # Placeholder for the word

    # insert letters
    for letter in sen:
        inputLetters.append(letter)

    # get word from letters
    count = 0
    for letter in inputLetters:
        if letter != " " and letter not in punctuations:
            constructWord = constructWord + letter
        elif letter == " ":
            words.append(constructWord)
            constructWord = ""

        count = count + 1
        if count == len(inputLetters): # check if last iteration
            words.append(constructWord)

    longest = words[0]

    # find the longest word in sentence
    for currentWord in range(len(words)):
        if len(words[currentWord]) > len(longest):
            longest = words[currentWord]

    return longest

print(LongestWord(yourWord))


valildword = input()


def pigLatin(word):
    firstLetter = word[0]
    vowels = ["a", "e", "i", "u"]
    newWord = ""
    if firstLetter in vowels:
        newWord = word + "way"
        print(newWord)
    else:
        newWord = word[1:] + word[0] + "ay"
        print(newWord)


pigLatin(valildword)

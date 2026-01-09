
def singleword(word):
    firstLetter = word[0]
    vowels = ["a", "e", "i", "u"]
    newWord = ""
    if firstLetter in vowels:
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"


validSentence = input()

wordList = validSentence.split()

newSentence = ""
for word in wordList:
    newSentence += singleword(word) + " "

print(newSentence)

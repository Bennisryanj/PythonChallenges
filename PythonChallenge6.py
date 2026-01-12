# My Solution


def ublang(word):
    letters = list(word)
    vowels = ["a", "e", "i", "u", "o"]
    newWord = ""
    for letter in letters:
        if letter in vowels:
            newWord += "ub" + letter
            print("hit")
        else:
            newWord += letter
            print("hit const")
    return newWord


validWord = input()

print(ublang(validWord))

# Book solution


def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter in 'aeiuo':
            output.append(f'ub{letter}')
        else:
            output.append(letter)

    return ''.join(output)


print(ubbi_dubbi('python'))

# My solution
sentence = list('cba')
newList = []
newWord = ""
for word in sentence:
    newList.append(word)
for word2 in sorted(newList):
    newWord += word2
print(newWord)

# book solution


def strsort(a_string):
    return ''.join(sorted(a_string))

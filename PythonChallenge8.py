# FirstLast write something that takes in a string, list or tuple that returns the first and last elements.

def firstLast(userInput):
    inputLen = len(userInput)
    return userInput[:1] + userInput[-1:]


listTest = [1, 2, 3, 4]

print(firstLast(listTest))

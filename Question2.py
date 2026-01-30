# Question 2
def string_length(stringList):
    resultDictionary = {}
    for string in stringList:
        stringLength = len(string)
        if stringLength % 2 == 0:
            parityType = "even"
        else:
            parityType = "odd"
        resultDictionary[string] = {
            "length": stringLength,
            "parity": parityType
        }
    return resultDictionary
testStrings = ["data", "science"]
print(string_length(testStrings))


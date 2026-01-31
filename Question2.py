# Question 2
# Function that analyzes a list of strings and returns their lengths and parity (even or odd).
def string_length(stringList):
    resultDictionary = {}
    for string in stringList:
        # Find the length of the string
        stringLength = len(string)
        # Checks if the string is even or odd
        if stringLength % 2 == 0:
            parityType = "even"
        else:
            parityType = "odd"
        # Stores the length and parity in the dictionary for this string
        resultDictionary[string] = {
            "length": stringLength,
            "parity": parityType
        }
    return resultDictionary
testStrings = ["data", "science"]
print(string_length(testStrings))


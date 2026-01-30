# Question 6
def percentageDictionary(numbers):
    resultDictionary = {}
    total_of_elements = len(numbers)

    # Get unique values and sort them
    uniqueValues = sorted(set(numbers))
    # Calculate percentage for each unique value
    for value in uniqueValues:
        countLessOrEqual = 0
        for number in numbers:
            if number <= value:
                countLessOrEqual += 1
        percentage = countLessOrEqual / total_of_elements * 100
        resultDictionary[value] = percentage
    return resultDictionary

numbers = [3, 1, 2, 3, 4, 2]
percentage = percentageDictionary(numbers)
print(percentage)
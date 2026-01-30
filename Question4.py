# Question 4
from random import random

# Generate a list of 20 random numbers between 0 and 1
values = [random() for i in range(20)]
# Generate random value for x
x = random()
# sort the list
sortedValues = sorted(values)
# Find all indices where the value is greater than or equal to x
matchingIndices = []

for index in range(len(sortedValues)):
    if sortedValues[index] >= x:
        matchingIndices.append(index)
# Print the sorted values
print("Sorted Values:")
print(sortedValues)
# Print the value of x
print("Value of x: ")
print(x)
# Print the first matching index if one exists
if len(matchingIndices) > 0:
    print("First index where value is greater than or equal to x:")
    print(matchingIndices[0])
else:
    print("No values are greater than or equal to x:")


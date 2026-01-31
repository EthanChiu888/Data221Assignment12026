# Question 1
# This file multiplies consecutive integers starting from 1 until the product first becomes greater than a given threshold value
# Stores the threshold value that the product must exceed
thresholdValue = 100
# Stores the running product of consecutive integers
currentProduct = 1
# Keeps track of the current integer being multiplied
currentMultiplier = 1
# Continues to loop as long as the product is less than or equal to the threshold value
while currentProduct <= thresholdValue:
    currentMultiplier += 1
    currentProduct *= currentMultiplier
print("Final Product: ", currentProduct)
print("The integer that caused the product to exceed the threshold", currentMultiplier )

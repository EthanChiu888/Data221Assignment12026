# This program multiplies consecutive integers starting from 1
# until the product becomes bigger than the threshold value

# Variable stores the threshold value
thresholdValue = 100


currentProduct = 1
currentMultiplier = 1

while currentProduct <= thresholdValue:
    currentMultiplier += 1
    currentProduct *= currentMultiplier
print("Final Product: ", currentProduct)
print("The integer that caused the product to exceed the threshold", currentMultiplier )

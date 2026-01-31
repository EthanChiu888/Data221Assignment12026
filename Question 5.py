# Question 5
#Calculates the percentage of the larger circle’s area that can be covered by the smaller circle, with input validation.
import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    # Validate inputs: must be positive integers
    if not isinstance(radiusOfCircle1, int) or not isinstance(radiusOfCircle2, int):
        return "Error: Radii must be integers."
    #Validate if both radii are positive
    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "Error: Radii must be positive integers."

    # Compute areas of both circles
    area1 = math.pi * (radiusOfCircle1 ** 2)
    area2 = math.pi * (radiusOfCircle2 ** 2)

    # Determine smaller and larger area
    smallerArea = min(area1, area2)
    largerArea = max(area1, area2)
    #Compute and print the percentage coverage
    percentageCoverage = (smallerArea / largerArea) * 100
    print(f"The area of coverage of the larger circle is {percentageCoverage:.2f}%")

circleAreaCoverage(10, 20)


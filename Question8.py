# Question 8
# Creates a pandas DataFrame and adds a computed column derived from existing data.
import pandas as pd

data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}
# Creates a data frame
dataFrame = pd.DataFrame(data)

dataFrame["A_times_B"] = dataFrame["A"] * dataFrame["B"]
dataFrame["A_times_C"] = dataFrame["A"] * dataFrame["C"]
print(dataFrame)
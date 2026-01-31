# Question 3
# Computes x^y for a list of (x, y) pairs, skipping any pairs with negative exponents.
def exponential_function(x,y):
    return x**y
# List of (x,y) pairs
pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
# List to store valid results
result = []
for x,y in pairs:
    # Skip negative exponents
    if y <0:
        continue
    result.append(exponential_function(x,y))
# Prints the result
print(result)







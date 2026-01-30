# Question 3
def exponential_function(x,y):
    return x**y
pairs = [(2, 3), (4, 1), (3, -2)]
resultList = []
for x, y in pairs:
    if y<0:
        continue
    result = exponential_function(x,y)
    resultList.append(result)
print(resultList)







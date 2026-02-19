import numpy as np
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
max_product = 0
for i in range(len(numbers)):
    for j in range(i+1 , len(numbers)):
        if numbers[i] * numbers[j] > max_product:
            max_product = numbers[i] * numbers[j]
print(max_product)

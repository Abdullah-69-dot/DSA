duplicatenumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 10]
unique_numbers = []
for i in duplicatenumbers:
    if duplicatenumbers.count(i) == 1:
        unique_numbers.append(i)
print(unique_numbers)
    
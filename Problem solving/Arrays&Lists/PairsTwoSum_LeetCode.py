list1 = [2, 7, 11, 15]
target = 9
for i in range(len(list1)):
    for j in range (i+1, len(list1)):
        if list1[i] + list1[j] == target:
            print(i, j)
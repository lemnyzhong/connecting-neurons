# initializing array
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

# concatenating arrays
# print(arr1 + arr2)

arr3 = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]

# 2-dimensional array access
# print(arr3)
# print(arr3[0])
# print(arr3[0][1])

arr4 = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
        [[10, 11, 12], [13, 14, 15], [16, 17, 18]], 
        [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]

# multi-dimensional array access
# print(arr4)
# print(arr4[0])
# print(arr4[0][1])
# print(arr4[0][1][2])

# for i in arr4:
#     # print(i)
#     for j in i:
#         # print(j)
#         for k in j:
#             print(k)

# appending array of arrays to array
arr4.append([[28, 29, 30], [31, 32, 33], [34, 35, 36]])


# iterates through each element of each array 
# in each array in the array
for i in arr4:
    # print(i)
    for j in i:
        # print(j)
        for k in j:
            print(k)

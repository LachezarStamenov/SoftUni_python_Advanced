# Write a program that receives a matrix and prints the flattened version of it (a list with all the values).
# For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
# On the first line, you will receive the number of a matrix's rows. On the next rows, you will get the elements for
# each column separated with a comma and a space ", ".

# first solution
rows = int(input())
result = []

for _ in range(rows):
    nums = [int(el) for el in input().split(", ")]
    result.extend(nums)
print(result)

# Second solution
# rows = int(input())
#
# matrix = []
# for _ in range(rows):
#     nums = [int(el) for el in input().split(", ")]
#     matrix.append(nums)
#
# result = []
#
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         result.append(matrix[row_index][col_index])
# print(result)
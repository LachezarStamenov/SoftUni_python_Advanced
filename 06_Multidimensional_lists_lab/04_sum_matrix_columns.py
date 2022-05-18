# Write a program that reads a matrix from the console and prints the sum for each column. On the first line, you will
# get the matrix's rows. On the next rows, you will get elements for each column separated with a space.

rows, cols = [int(el) for el in input().split(', ')]
matrix = []
result = 0
for _ in range(rows):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)

for col_index in range(cols):
    result = 0
    for row_index in range(rows):
        result += matrix[row_index][col_index]
    print(result)

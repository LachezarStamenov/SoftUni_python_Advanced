# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its
# elements. There will be no case with two or more 3x3 squares with equal maximal sum.
# Input
# •	On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the range
# [1, 20]
# •	On the following lines, you will receive each row with its columns - integers, separated by a single space in the
# range [-20, 20]
# Output
# •	On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
# •	On the following 3 lines, print each element of the found submatrix, separated by a single space

rows, cols = [int(x) for x in input().split()]

matrix = []


for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = float('-inf')
best_row = 0
best_col = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col] \
                      + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + matrix[row + 2][col] \
                      + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            best_row = row
            best_col = col
print(f"Sum = {max_sum}")
print(f"{matrix[best_row][best_col]} {matrix[best_row][best_col + 1]} {matrix[best_row][best_col + 2]}")
print(f"{matrix[best_row + 1][best_col]} {matrix[best_row + 1][best_col + 1]} {matrix[best_row + 1][best_col + 2]}")
print(f"{matrix[best_row + 2][best_col]} {matrix[best_row + 2][best_col + 1]} {matrix[best_row + 2][best_col + 2]}")

# second solution
# max_sum = None
#
# rows, cols = [int(x) for x in input().split()]
#
# matrix = [[x for x in input().split()] for _ in range(rows)]
#
# for i in range(rows - 2):
#     for j in range(cols - 2):
#         sub_matrix = [matrix[r][j:j + 3] for r in range(i, i + 3)]
#         temp_sum = sum([int(x) for row in sub_matrix for x in row])
#         if not max_sum or temp_sum > max_sum:
#             max_sum = temp_sum
#             output_matrix = sub_matrix.copy()
#
# print(f'Sum = {max_sum}')
# for row in output_matrix:
#     print(' '.join([str(x) for x in row]))

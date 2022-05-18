# Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with biggest sum of its
# values.
# On first line you will get matrix sizes in format "{rows}, {columns}".  On the next rows, you will get elements for
# each column, separated with a comma and a space ", ".
# You should print the found submatrix and the sum of its elements, as shown in the examples.


rows, cols = [int(el) for el in input().split(", ")]

matrix = []
for _ in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

max_sum = -99999999999
max_sum_matrix = []

for row_index in range(rows - 1):
    for column_index in range(cols - 1):
        sub_matrix = [matrix[row_index][column_index], matrix[row_index][column_index + 1],
                      matrix[row_index +1][column_index], matrix[row_index + 1][column_index + 1]]

        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_matrix = sub_matrix.copy()
print(max_sum_matrix[0], max_sum_matrix[1])
print(max_sum_matrix[2], max_sum_matrix[3])
print(max_sum)
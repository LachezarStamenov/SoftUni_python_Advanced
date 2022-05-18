# Write a program that reads a matrix from the console and performs certain operations with its elements. User input is
# provided similarly to the problems above - first, you read the dimensions and then the data.
# Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and
# ("row2", "col2") are the coordinates of two points in the matrix. A valid command starts with the "swap" keyword along
# with four valid coordinates (no more, no less), separated by a single space.
# •	If the command is valid, you should swap the values at the given indexes and print the matrix at each step (thus,
# you will be able to check if the operation was performed correctly).
# •	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered, or the
# given coordinates are not valid), print "Invalid input!" and move on to the following command. A negative value makes
# the coordinates not valid.
# Your program should finish when the command "END" is entered.

def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == "END":
        break

    command = line.split()[0]

    if len(line.split()) != 5 or command != "swap":
        print('Invalid input!')

    row1, col1, row2, col2 = [int(x) for x in (line.split()[1:])]

    if is_outside(row1, col1, rows, cols) or is_outside(row2, col2, rows, cols):
        print('Invalid input!')
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(*row, sep=' ')

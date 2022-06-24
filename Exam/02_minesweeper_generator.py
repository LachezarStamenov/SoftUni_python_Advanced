# You will be given an integer n for the size of the mines field with square shape and another one for the number of
# bombs that you have to place in the field. On the next n lines, you will receive the position for each bomb. Your
# task is to create the game field placing the bombs at the correct positions and mark them with "*", and calculate
# the numbers in each cell of the field. Each cell represents a number of all bombs directly near it (up, down, left,
# right and the 4 diagonals).
# Input
# •	On the first line, you are given the integer n – the size of the square matrix.
# •	On the second line – the number of the bombs.
# •	The next n lines holds the position of each bomb.
# Output
# •	Print the matrix you've created.
# Constraints
# •	The size of the square matrix will be between [2…15].
#
def is_inside(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True

def calculate_cell_value(matrix, row, col, size):
    bombs_count = 0

    if is_inside(row - 1, col, size):
        if matrix[row - 1][col] == "*":
            bombs_count += 1
    if is_inside(row + 1, col, size):
        if matrix[row + 1][col] == '*':
            bombs_count += 1
    if is_inside(row, col - 1, size):
        if matrix[row][col - 1] == '*':
            bombs_count += 1
    if is_inside(row, col + 1, size):
        if matrix[row][col + 1] == '*':
            bombs_count += 1
    if is_inside(row - 1, col + 1, size):
        if matrix[row - 1][col + 1] == '*':
            bombs_count += 1
    if is_inside(row + 1, col + 1, size):
        if matrix[row + 1][col + 1] == '*':
            bombs_count += 1
    if is_inside(row - 1, col - 1, size):
        if matrix[row - 1][col - 1] == '*':
            bombs_count += 1
    if is_inside(row + 1, col - 1, size):
        if matrix[row + 1][col - 1] == '*':
            bombs_count += 1
    return bombs_count


size = int(input())
bombs = int(input())

matrix = [[0 for j in range(size)] for i in range(size)]

for bomb in range(bombs):
    bomb_pos_row, bomb_pos_col = map(lambda x: int(x), input()[1:][:-1].split(', '))
    matrix[bomb_pos_row][bomb_pos_col] = "*"

for row in range(size):
    for col in range(size):
        element = matrix[row][col]
        if element == '*':
            continue
        else:
            matrix[row][col] = calculate_cell_value(matrix, row, col, size)
for row in matrix:
    print(*row, sep=' ')


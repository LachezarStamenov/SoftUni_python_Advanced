# You will be given a square matrix of integers, each integer separated by a single space, and each row will be on a new
# line. On the last line of input, you will receive indexes - coordinates of several cells separated by a single space,
# in the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}".
# On those cells, there are bombs. You must detonate every bomb in the order they were given. When a bomb explodes, it
# deals damage equal to its integer value to all the cells around it (in every direction and in all diagonals). One bomb
# can't explode more than once, and after it does, its value becomes 0. When a cell's value reaches 0 or below, it dies.
# Dead cells can't explode.
# You must print the count of all alive cells and their sum. Afterward, print the matrix with all its cells (including
# the dead ones).
# Input
# •	On the first line, you are given the integer N - the size of the square matrix.
# •	The following N lines hold each column's values - N numbers separated by a space.
# •	On the last line, you will receive the coordinates of the cells with the bombs in the format described above.
# Output
# •	On the first line, you need to print the count of all alive cells in the format:
# "Alive cells: {alive_cells}"
# •	On the second line, you need to print the sum of all alive cells in the format:
# "Sum: {sum_of_cells}"
# •	In the end, print the matrix. A space must separate the cells.
# Constraints
# •	The size of the matrix will be between [0…1000].
# •	The bomb coordinates will always be in the matrix.
# •	The bomb's values will always be greater than 0.
# •	The integers of the matrix will be in the range [1…10000].
def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_neighbors(row, col, matrix):
    size = len(matrix)
    neighbors = []
    # row - 1, col
    if is_inside(row - 1, col, size) and matrix[row - 1][col] > 0:
        neighbors.append([row - 1, col])
    # row + 1, col
    if is_inside(row + 1, col, size) and matrix[row + 1][col] > 0:
        neighbors.append([row + 1, col])
    # row, col - 1
    if is_inside(row, col - 1, size) and matrix[row][col - 1] > 0:
        neighbors.append([row, col - 1])
    # row, col + 1
    if is_inside(row, col + 1, size) and matrix[row][col + 1] > 0:
        neighbors.append([row, col + 1])
    # row - 1, col - 1
    if is_inside(row - 1, col - 1, size) and matrix[row - 1][col - 1] > 0:
        neighbors.append([row - 1, col - 1])
    # row - 1, col + 1
    if is_inside(row - 1, col + 1, size) and matrix[row - 1][col + 1] > 0:
        neighbors.append([row - 1, col + 1])
    #  row + 1, col - 1
    if is_inside(row + 1, col - 1, size) and matrix[row + 1][col - 1] > 0:
        neighbors.append([row + 1, col - 1])
    #  row + 1, col - 1
    if is_inside(row + 1, col + 1, size) and matrix[row + 1][col + 1] > 0:
        neighbors.append([row + 1, col + 1])
    return neighbors


n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()

for bomb_coords in bombs:
    bomb_row, bomb_col = [int(x) for x in bomb_coords.split(',')]
    if matrix[bomb_row][bomb_col] <= 0:
        continue
    bomb_power = matrix[bomb_row][bomb_col]
    matrix[bomb_row][bomb_col] = 0
    neighbours = get_neighbors(bomb_row, bomb_col, matrix)

    for row, col in neighbours:
        matrix[row][col] -= bomb_power

alive_cells = 0
alive_cells_sum = 0
for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            alive_cells_sum += el
print(f'Alive cells: {alive_cells}')
print(f'Sum: {alive_cells_sum}')

for row in matrix:
    print(*row, sep=' ')
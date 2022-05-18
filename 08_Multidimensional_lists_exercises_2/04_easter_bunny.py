# Your task is to collect as many eggs as possible.
# On the first line, you will be given a number representing the size of the field. On the following few lines, you will
# be given a field with:
# •	One bunny - randomly placed in it and marked with the symbol "B"
# •	Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs. The
# directions that should be considered as possible are up, down, left, and right. If you reach a trap while checking
# some of the directions, you should not consider the fields after the trap in this direction. For more clarifications,
# see the examples below.
# Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
# Input
# •	A number representing the size of the field
# •	The matrix representing the field (each position separated by a single space)
# Output
# •	The direction which should be considered as best (lowercase)
# •	The field positions from which we are collecting eggs as lists
# •	The total number of eggs collected
# Constraints
# •	There will NOT be two or more paths consisting of the same total amount of eggs.
import current


def move_up(row, col):
    return row - 1, col


def move_down(row, col):
    return row + 1, col


def move_left(row, col):
    return row, col - 1


def move_right(row, col):
    return row, col + 1


size = int(input())
matrix = []

bunny_row = 0
bunny_col = 0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == 'B':
            bunny_row = row
            bunny_col = col

directions = {
    'right': move_right,
    'up': move_up,
    'left': move_left,
    'down': move_down
}

best_direction = ''
best_score = float('-inf')
best_path = []

for direction, step in directions.items():
    current_row, current_col = bunny_row, bunny_col
    current_score = 0
    path = []

    while True:
        current_row, current_col = step(current_row, current_col)

        if current_row < 0 or current_col < 0 or current_row >= size or current_col >= size:
            break
        if matrix[current_row][current_col] == 'X':
            break
        path.append([current_row, current_col])
        current_score += int(matrix[current_row][current_col])
    if current_score > best_score and path:
        best_score = current_score
        best_direction = direction
        best_path = path


print(best_direction)
for step in best_path:
    print(step)
print(best_score)

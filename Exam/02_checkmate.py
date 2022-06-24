def is_inside(row, col, matrix_size):
    return 0 <= row < matrix_size and 0 <= col < matrix_size


matrix_size = 8
matrix = []

for _ in range(matrix_size):
    matrix.append(input().split())

movement = {
    "up": lambda row, col: (row - 1, col),
    "down": lambda row, col: (row + 1, col),
    "left": lambda row, col: (row, col - 1),
    "right": lambda row, col: (row, col + 1),
    "up-right": lambda row, col: (row - 1, col + 1),
    "up-left": lambda row, col: (row - 1, col - 1),
    "down-right": lambda row, col: (row + 1, col + 1),
    "down-left": lambda row, col: (row + 1, col - 1)
}

player_path = []

for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == "Q":
            for move in movement:
                next_row, next_col = movement[move](row, col)
                while is_inside(next_row, next_col, matrix_size):
                    if matrix[next_row][next_col] == "Q":
                        break
                    if matrix[next_row][next_col] == "K":
                        player_path.append([row, col])
                        break
                    next_row, next_col = movement[move](next_row, next_col)
if len(player_path) == 0:
    print("The king is safe!")
else:
    print(*player_path, sep="\n")
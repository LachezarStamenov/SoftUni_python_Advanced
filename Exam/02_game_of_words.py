def get_next_pos(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


def is_inside(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


initial_string = input()
size = int(input())

matrix = []
rows = size
cols = size

player_pos_row = None
player_pos_col = None


for row in range(rows):
    row_elements = list(input())
    matrix.append(row_elements)

    for col in range(cols):
        if row_elements[col] == "P":
            player_pos_row = row
            player_pos_col = col

m = int(input())

for _ in range(m):
    command = input()

    next_pos_row, next_pos_col = get_next_pos(command, player_pos_row, player_pos_col)

    if is_inside(next_pos_row, next_pos_col, rows, cols):
        if matrix[next_pos_row][next_pos_col] == "-":
            pass
        else:
            collected_letter = matrix[next_pos_row][next_pos_col]
            initial_string += collected_letter
        matrix[next_pos_row][next_pos_col] = 'P'
        matrix[player_pos_row][player_pos_col] = '-'
        player_pos_row, player_pos_col = next_pos_row, next_pos_col
    else:
        if initial_string:
            initial_string = initial_string[:-1]

print(f"{initial_string}")
for row in matrix:
    print(*row, sep='')

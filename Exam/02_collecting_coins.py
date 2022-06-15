def check_if_is_outside(size, player_row, player_col):
    if player_row < 0:
        return size - 1, player_col
    elif player_col < 0:
        return player_row, size - 1
    elif player_row > size - 1:
        return 0, player_col
    elif player_col > size - 1:
        return player_row, 0
    else:
        return player_row, player_col


def get_next_pos(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


size = int(input())
matrix = []
player_row = None
player_col = None
collected_coins = 0
commands = ['up', 'down', 'left', 'right']
is_winner = False
path = []


for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == "P":
            player_row = row
            player_col = col
            path.append([player_row, player_col])
while True:
    if collected_coins >= 100:
        is_winner = True
        break

    current_command = input()
    if current_command not in commands:
        continue

    player_row, player_col = get_next_pos(current_command, player_row, player_col)
    player_row, player_col = check_if_is_outside(size, player_row, player_col)
    current_value = matrix[player_row][player_col]
    path.append([player_row, player_col])


    if current_value != 'P' and current_value != 'X':
        collected_coins += int(current_value)
        matrix[player_row][player_col] = 0

    elif current_value == 'X':
        collected_coins = collected_coins // 2
        break


if is_winner:
    print(f"You won! You've collected {collected_coins} coins.")
else:
    print(f"Game over! You've collected {collected_coins} coins.")
print(f"Your path:")
for el in path:
    print(el)

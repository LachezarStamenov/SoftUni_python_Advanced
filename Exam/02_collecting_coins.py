# On the first line, you will be given a number representing the size of the field with a square shape. On the
# following few lines, you will be given the field with:
# •	One player - randomly placed in it and marked with the symbol "P"
# •	Numbers for coins placed at different positions of the field
# •	Walls marked with "X"
# After the field state, you will be given commands for the player's movement. Commands can be: "up", "down", "left",
# "right". If the command is invalid, you should ignore it.
# The player moves in the given direction with one step for each command and collects all the coins that come across.
# If he goes out of the field, he should continue to traverse the field from the opposite side in the same direction.
# Note: He can go through the same path many times, but he can collect the coins just once (the first time).
# There are only two possible outcomes of the game:
# •	The player hits a wall, loses the game, and his coins are reduced to 50% and rounded down to the next-lowest number.
# •	The player collects at least 100 coins and wins the game.
# For more clarifications, see the examples below.
# Input
# •	A number representing the size of the field (matrix NxN)
# •	A matrix representing the field (each position separated by a single space)
# •	On each of the following lines, you will get a move command.
# Output
# •	If the player won the game, print: "You won! You've collected {total_coins} coins."
# •	If the player loses the game, print: "Game over! You've collected {total_coins} coins."
# •	Collected coins have to be rounded down to the next-lowest number.
# •	The player's path as cooridnates in lists on separate lines:
# "Your path:
# [{row_position1}, {column_position1}]
# [{row_position2}, {column_position2}]
# …
# [{row_positionN}, {column_positionN}]"
# Constrains
# •	There will be no case in which less than 100 coins will be in the field
# •	All given numbers will be valid integers in the range [0, 100]


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

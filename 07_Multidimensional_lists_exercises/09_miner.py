# You are going to create a game called "Miner".
# First, you will receive the size of a square field in which the miner should move.
# On the second line, you will receive the commands for the miner's movement, separated by a single space. The possible
# commands are "left", "right", "up" and "down".
# In the end, you will receive each row of the field on a separate line. The possible characters that may appear on the
# screen are:
# •	* - a regular position on the field
# •	e - the end of the route
# •	c - coal
# •	s - miner
# The miner starts moving from the position "s". He should perform the given commands successively, moving with only one
# position in the given direction. If the miner has reached the edge of the field and the following command indicates
# that he has to get out of the area, he must remain in his current position and ignore the command.
# When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal. In the end, you
# should print whether the miner has succeeded in collecting the coal or not and his final position:
# •	If the miner has collected all coal in the field, the program stops, and you should print the message: "You
# collected all coal! ({row_index}, {col_index})".
# •	If the miner steps at "e", the game is over (the program stops), and you should print the message: "Game over!
# ({row_index}, {col_index})".
# •	If there are no more commands and none of the above cases had happened, you should print the message:
# "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
# Input
# •	Field size - an integer number
# •	Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
# •	The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
# Output
# •	There are three types of output as mentioned above.
# Constraints
# •	The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
# •	The field will always have only one "s"
def get_next_pos(command, row, col):
    if command == "up":
        return row - 1, col
    if command == "left":
        return row, col - 1
    if command == "right":
        return row, col + 1
    if command == "down":
        return row + 1, col


n = int(input())

commands = input().split()
matrix = []

miner_row = 0
miner_col = 0
total_coal = 0

for row in range(n):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(n):
        element = row_elements[col]
        if element == 's':
            miner_row = row
            miner_col = col
        elif element == 'c':
            total_coal += 1
game_over = False

for command in commands:
    next_row, next_col = get_next_pos(command, miner_row, miner_col)

    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
        continue

    miner_row, miner_col = next_row, next_col
    if matrix[miner_row][miner_col] == 'c':
        matrix[miner_row][miner_col] = '*'
        total_coal -= 1

        if total_coal == 0:
            break
    elif matrix[miner_row][miner_col] == 'e':
        game_over = True
        break

if total_coal == 0:
    print(f'You collected all coal! ({miner_row}, {miner_col})')
elif game_over:
    print(f'Game over! ({miner_row}, {miner_col})')
else:
    print(f'{total_coal} pieces of coal left. ({miner_row}, {miner_col})')








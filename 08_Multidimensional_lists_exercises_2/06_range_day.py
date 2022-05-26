# You are participating in a Firearm course. It is a training day at the shooting range.
# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by
# a single space:
# •	Your position is marked with the symbol "A"
# •	Targets marked with symbol "x"
# •	All of the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands you will receive. The possible
# commands are:
# •	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only move
# if the field you want to step on is marked with ".".
# •	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving).
# Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot
# only the nearest target. When you have shot a target, the field becomes empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
# •	If at any point there are no targets left, end the program and print: "Training completed! All {count_targets}
# targets hit.".
# •	If, after you perform all the commands, there are some targets left print: "Training not completed!
# {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit, as shown in the examples.
# Input
# •	5 lines representing the field (symbols, separated by a single space)
# •	N - count of commands
# •	On the following N lines - the commands in the format described above
# Output
# •	On the first line, print one of the following:
# o	If all the targets were shot
# "Training completed! All {count_targets} targets hit."
# o	Otherwise:
#  "Training not completed! {count_left_targets} targets left."
# •	Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.
# Constrains
# •	All the commands will be valid
# •	There will always be at least one target

def get_next_pos(direction, row, col, steps):
    if direction == 'up':
        return row - steps, col
    if direction == 'down':
        return row + steps, col
    if direction == 'left':
        return row, col - steps
    if direction == 'right':
        return row, col + steps


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


size = 5
matrix = []

player_row = 0
player_col = 0
total_targets = 0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == 'x':
            total_targets += 1
        elif row_elements[col] == 'A':
            player_row = row
            player_col = col

targets_left = total_targets

n = int(input())
hit_targets = []

for _ in range(n):
    command_args = input().split()
    command = command_args[0]
    direction = command_args[1]

    if command == 'move':
        steps = int(command_args[2])
        next_row, next_col = get_next_pos(direction, player_row, player_col, steps)

        if is_outside(next_row, next_col, size) or matrix[next_row][next_col] != '.':
            continue
        matrix[player_row][player_col] = '.'
        player_row, player_col = next_row, next_col
        matrix[player_row][player_col] = 'А'
    else:
        bullet_row, bullet_col = player_row, player_col
        while True:
            bullet_row, bullet_col = get_next_pos(direction, bullet_row, bullet_col, 1)

            if is_outside(bullet_row, bullet_col, size):
                break
            if matrix[bullet_row][bullet_col] == 'x':
                targets_left -= 1
                hit_targets.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = '.'
                break
        if targets_left == 0:
            break

if targets_left == 0:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {targets_left} targets left.")

for hit_target in hit_targets:
    print(hit_target)

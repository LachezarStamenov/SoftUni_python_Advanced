# Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
# You will receive a 6x6 field on separate lines with:
# •	One rover - marked with the letter "E"
# •	Water deposit (one or many) - marked with the letter "W"
# •	Metal deposit (one or many) - marked with the letter "M"
# •	Concrete deposit (one or many) - marked with the letter "C"
# •	Rock (one or many) - marked with the letter "R"
# •	Empty positions will be marked with "-"
# After that, you will be given the commands for the rover's movement on one line separated by a comma and a space
# (", "). Commands can be: "up", "down", "left", or "right".
# For each command, the rover moves in the given directions with one step, and it can land on one of the given types
# of deposit or a rock:
# •	When it lands on a deposit, you must print the coordinates of that deposit in the format shown below and increase
# its value by 1.
# •	If the rover lands on a rock, it gets broken. Print the coordinates where it got broken in the format shown below,
# and the program ends.
# •	If the rover goes out of the field, it should continue from the opposite side in the same direction. Example: If
# the rover is at position (3, 0) and it needs to move left (outside the matrix), it should be placed at position
# (3, 5).
# The rover needs to find at least one of each deposit to consider the area suitable to start our colony.
# Stop the program if you run out of commands or the rover gets broken.
# Input
# •	On the first 6 lines, you will receive the matrix.
# •	On the following line, you will receive the commands for the rover separated by a comma and a space.
# Output
# •	For each deposit found while you go through the commands, print out on the console: "{Water, Metal or Concrete}
# deposit found at ({row}, {col})"
# •	If the rover hits a rock, print the coordinates where it got broken in the format: "Rover got broken at ({row},
# {col})"
# After you go through all the commands or the rover gets broken, print out on the console:
# •	If the rover has found at least one of each deposit, print on the console: "Area suitable to start the colony."
# •	Otherwise, print on the console: "Area not suitable to start the colony."
# See examples for more clarification.


def get_next_position(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


def is_outside(row, col, size):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True


matrix = []

size = 6
rover_row = 0
rover_col = 0
deposits = {'water': 0, 'metal': 0, 'concrete': 0}
sum_deposits = 0
for row in range(6):
    row_elements = list(input().split())
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == "E":
            rover_row = row
            rover_col = col


commands = list(input().split(', '))

for command in commands:
    rover_row, rover_col = get_next_position(command, rover_row, rover_col)

    if is_outside(rover_row, rover_col, size):
        if rover_row < 0:
            rover_row = 5
        elif rover_row > 5:
            rover_row = 0
        if rover_col < 0:
            rover_col = 5
        elif rover_col > 5:
            rover_col = 0
    cell_value = matrix[rover_row][rover_col]

    if cell_value == "W":
        print(f"Water deposit found at {rover_row, rover_col}")
        deposits['water'] += 1
    elif cell_value == "M":
        print(f"Metal deposit found at {rover_row, rover_col}")
        deposits['metal'] += 1
    elif cell_value == "C":
        print(f"Concrete deposit found at {rover_row, rover_col}")
        deposits['concrete'] += 1
    elif cell_value == "R":
        print(f"Rover got broken at {rover_row, rover_col}")
        break


if 0 in deposits.values():
    print("Area not suitable to start the colony.")
else:
    print("Area suitable to start the colony. ")


# second solution
# def move_rover(direction, row, col):
#     if direction == 'left':
#         return row, col - 1
#     if direction == 'right':
#         return row, col + 1
#     if direction == 'up':
#         return row - 1, col
#     if direction == 'down':
#         return row + 1, col
#
#
# def is_outside(row, col, size):
#     return row < 0 or col < 0 or row >= size or col >= size
#
#
# def reposition_rover(row, col, size):
#     if row < 0:
#         return size - 1, col
#     if row >= size:
#         return 0, col
#     if col < 0:
#         return row, size - 1
#     if col >= size:
#         return row, 0
#
#
# rover_row, rover_col = 0, 0
#
# size = 6
# area = []
# for row in range(size):
#     row_elements = input().split()
#     for col in range(size):
#         if row_elements[col] == 'E':
#             rover_row, rover_col = row, col
#     area.append(row_elements)
#
# directions = input().split(", ")
#
# water_found = False
# metal_found = False
# concrete_found = False
# for direction in directions:
#     rover_row, rover_col = move_rover(direction, rover_row, rover_col)
#
#     if is_outside(rover_row, rover_col, size):
#         rover_row, rover_col = reposition_rover(rover_row, rover_col, size)
#
#     cell_value = area[rover_row][rover_col]
#     if cell_value == 'W':
#         water_found = True
#         print(f'Water deposit found at ({rover_row}, {rover_col})')
#     elif cell_value == 'M':
#         metal_found = True
#         print(f'Metal deposit found at ({rover_row}, {rover_col})')
#     elif cell_value == 'C':
#         concrete_found = True
#         print(f'Concrete deposit found at ({rover_row}, {rover_col})')
#     elif cell_value == 'R':
#         print(f'Rover got broken at ({rover_row}, {rover_col})')
#         break
#
# if water_found and metal_found and concrete_found:
#     print('Area suitable to start the colony.')
# else:
#     print('Area not suitable to start the colony.')
# You are visiting Santa Claus' workshop, and it is complete chaos. You will need to help Santa find all items
# scattered around the workshop.
# You will be given the size of the matrix in the format "{rows}, {columns}". It is the Santa's workshop represented
# as some symbols separated by a single space:
# •	Your position is marked with the symbol "Y"
# •	Christmas decorations are marked with the symbol "D"
# •	Gifts are marked with the symbol "G"
# •	Cookies are marked with the symbol "C"
# •	All of the empty positions will be marked with "."
# After the field state, you will be given commands until you receive the command "End". The commands will be in the
# format "right/left/up/down-{steps}". You should move in the given direction with the given steps and collect all the
# items that come across. If you go out of the field, you should continue to traverse the field from the opposite side
# in the same direction. You should mark your path with "x". Your current position should always be marked with "Y".
# Keep track of all collected items. If you've collected all items at any point, end the program and print: "Merry
# Christmas!".
# Input
# •	On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
# •	On the next lines, you will receive each row with its columns - symbols, separated by a single space.
# •	On the following lines, you will receive commands in the format described above until you receive the command "End"
# or until you collect all items.
# Output
# •	On the first line, if you have collected all items, print:
# o	"Merry Christmas!"
# o	Otherwise, skip the line
# •	Next, print the number of collected items in the format:
# o	"You've collected:
# o	- {number_of_decoration} Christmas decorations
# o	- {number_of_gifts} Gifts
# o	- {number_of_cookies} Cookies"
# •	Finally, print the field, as shown in the examples.
# Constrains
# •	All the commands will be valid
# •	There will always be at least one item
# •	The dimensions of the matrix will be integers in the range [1, 20]
# •	The field will always have only one "Y"
# •	On the field, there will always be only the symbols shown above.
# def get_next_pos(direction, row, col, steps):
#     if direction == 'up':
#         return row - steps, col
#     if direction == 'down':
#         return row + steps, col
#     if direction == 'left':
#         return row, col - steps
#     if direction == 'right':
#         return row, col + steps
def get_next_pos(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


def is_outside(rows, cols, my_pos_row, my_pos_col):
    if my_pos_row < 0:
        return rows - 1, my_pos_col
    elif my_pos_col < 0:
        return my_pos_row, cols - 1
    elif my_pos_row > rows - 1:
        return 0, my_pos_col
    elif my_pos_col > cols - 1:
        return my_pos_row, 0
    else:
        return my_pos_row, my_pos_col


def check_for_subject(matrix, my_pos_row, my_pos_col, gifts):
    if matrix[my_pos_row][my_pos_col] == "D":
        gifts['decorations'] += 1
    elif matrix[my_pos_row][my_pos_col] == "G":
        gifts['gifts'] += 1
    elif matrix[my_pos_row][my_pos_col] == "C":
        gifts['cookies'] += 1
    return gifts
rows, cols = [int(x) for x in input().split(', ')]

matrix = []
my_pos_row = 0
my_pos_col = 0
total_subjects = 0
walk_end = False
gifts = {'decorations': 0,
         'gifts': 0,
         'cookies': 0
         }

for row in range(rows):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(cols):
        if row_elements[col] == "Y":
            my_pos_row = row
            my_pos_col = col
        if row_elements[col] != '.' and row_elements[col] != 'Y':
            total_subjects += 1

matrix[my_pos_row][my_pos_col] = 'x'

while True:
    current_command = input()
    if current_command == 'End':
        matrix[my_pos_row][my_pos_col] = 'Y'
        break

    direction = current_command.split('-')[0]
    steps = int(current_command.split('-')[1])

    for step in range(steps):
        my_pos_row, my_pos_col = get_next_pos(direction, my_pos_row, my_pos_col)
        if is_outside:
            my_pos_row, my_pos_col = is_outside(rows, cols, my_pos_row, my_pos_col)
            check_for_subject(matrix, my_pos_row, my_pos_col, gifts)
            matrix[my_pos_row][my_pos_col] = 'x'
            if sum(gifts.values()) == total_subjects:
                matrix[my_pos_row][my_pos_col] = 'Y'
                walk_end = True
                break
    if walk_end:
        break
if sum(gifts.values()) == total_subjects:
    print("Merry Christmas!")
print(f"You've collected:")
print(f"- {gifts.get('decorations')} Christmas decorations")
print(f"- {gifts.get('gifts')} Gifts")
print(f"- {gifts.get('cookies')} Cookies")

for row in matrix:
    print(*row, sep=" ")

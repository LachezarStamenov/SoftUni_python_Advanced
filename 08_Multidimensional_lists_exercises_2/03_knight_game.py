# Chess is the oldest game, but it is still popular these days. It will be used only one chess piece for this task -
# the Knight.
# A chess knight has 8 possible moves it can make, as illustrated. It can move to the nearest square but not on the
# same row, column, or diagonal. (e.g., it can move two squares horizontally, then one square vertically, or it can
# move one square horizontally then two squares vertically - i.e., in an "L" pattern.)
# The knight game is played on a board with dimensions N x N.
# You will receive a board with "K" for knights and "0" for empty cells. Your task is to remove knights until no
# knights that can attack one another with one move are left.
# Input
# •	On the first line, you will receive integer N - the size of the board
# •	On the following N lines, you will receive strings with "K" and "0"
# Output
# •	Print a single integer with the minimum number of knights that need to be removed
def is_knight(row, col, matrix):
    return matrix[row][col] == 'K'

def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_attack_counter(row, col, matrix):
    result = 0
    if is_inside(row - 2, col - 1, len(matrix)) and is_knight(row - 2, col - 1, matrix):
        result += 1
    if is_inside(row - 2, col + 1, len(matrix)) and is_knight(row - 2, col + 1, matrix):
        result += 1
    if is_inside(row - 1, col - 2, len(matrix)) and is_knight(row - 1, col - 2, matrix):
        result += 1
    if is_inside(row - 1, col + 2, len(matrix)) and is_knight(row - 1, col + 2, matrix):
        result += 1
    if is_inside(row + 2, col - 1, len(matrix)) and is_knight(row + 2, col - 1, matrix):
        result += 1
    if is_inside(row + 2, col + 1, len(matrix)) and is_knight(row + 2, col + 1, matrix):
        result += 1
    if is_inside(row + 1, col - 2, len(matrix)) and is_knight(row + 1, col - 2, matrix):
        result += 1
    if is_inside(row + 1, col + 2, len(matrix)) and is_knight(row + 1, col + 2, matrix):
        result += 1
    return result


size = int(input())

matrix = []
for _ in range(size):
    matrix.append(list(input()))

removed_knights = 0

while True:
    table = {}
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == '0':
                continue
            counter = get_attack_counter(row, col, matrix)
            if counter:
                table[(row, col)] = counter
    if len(table) == 0:
        break

    best_counter = 0
    knight_row, knight_col = 0, 0

    for coords, counter in table.items():
        if counter > best_counter:
            best_counter = counter
            knight_row = coords[0]
            knight_col = coords[1]
    matrix[knight_row][knight_col] = '0'
    removed_knights += 1


print(removed_knights)


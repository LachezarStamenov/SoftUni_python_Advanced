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

def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


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



def get_neighbors(row, col, matrix):
    size = len(matrix)
    neighbors = []
    # row - 1, col
    if is_inside(row - 1, col, size) and matrix[row - 1][col] > 0:
        neighbors.append([row - 1, col])
    # row + 1, col
    if is_inside(row + 1, col, size) and matrix[row + 1][col] > 0:
        neighbors.append([row + 1, col])
    # row, col - 1
    if is_inside(row, col - 1, size) and matrix[row][col - 1] > 0:
        neighbors.append([row, col - 1])
    # row, col + 1
    if is_inside(row, col + 1, size) and matrix[row][col + 1] > 0:
        neighbors.append([row, col + 1])
    # row - 1, col - 1
    if is_inside(row - 1, col - 1, size) and matrix[row - 1][col - 1] > 0:
        neighbors.append([row - 1, col - 1])
    # row - 1, col + 1
    if is_inside(row - 1, col + 1, size) and matrix[row - 1][col + 1] > 0:
        neighbors.append([row - 1, col + 1])
    #  row + 1, col - 1
    if is_inside(row + 1, col - 1, size) and matrix[row + 1][col - 1] > 0:
        neighbors.append([row + 1, col - 1])
    #  row + 1, col - 1
    if is_inside(row + 1, col + 1, size) and matrix[row + 1][col + 1] > 0:
        neighbors.append([row + 1, col + 1])
    return neighbors
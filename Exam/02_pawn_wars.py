# A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8, and columns are
# marked from A to H. We have a total of 64 squares. Each square is represented by a combination of letters and a
# number (a1, b1, c1, etc.). In this problem colors of the board will be ignored.
# We will play the game with two pawns, white (w) and black (b), where they can:
# •	Only move forward in a straight line:
# 	White (w) moves from the 1st rank to the 8th rank direction.
# 	Black (b) moves from 8th rank to the 1st rank direction.
# •	Can move only 1 square at a time.
# •	Can capture another pawn in from of them only diagonally:
# Some rules apply when moving paws:
# •	If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn. When a pawn
# captures another pawn, the game is over.
# •	If no capture is possible, the pawns keep on moving until one of them reaches the last rank.
# Input
# •	On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
# o	Empty positions are marked with "-".
# o	White pawn is marked with "w"
# o	Black pawn is marked with "b"
# Output
# Print either one of the following:
# •	If a pawn captures the other, print:
# o	"Game over! {White/Black} win, capture on {square}."
# •	If a pawn reaches the last rank, print:
# o	"Game over! {White/Black} pawn is promoted to a queen at {square}."
# Constraints
# •	The input will always be valid.
# •	The matrix will always be 8x8.
# •	There will be no case where two pawns are placed on the same square.
# •	There will be no case where two pawns are placed on the same column.
# •	There will be no case where black/white will be placed on the last rank.

def check_if_can_capture(coordinates_attacker, coordinates_defender):
    row_a = coordinates_attacker[0]
    col_a = coordinates_attacker[1]
    row_d = coordinates_defender[0]
    col_d = coordinates_defender[1]
    if row_a - 1 >= 0 and col_a - 1 >= 0:
        if row_a - 1 == row_d and col_a - 1 == col_d:
            return [row_a - 1, col_a - 1]
    if row_a - 1 >= 0 and col_a + 1 < 8:
        if row_a - 1 == row_d and col_a + 1 == col_d:
            return [row_a - 1, col_a + 1]
    if row_a + 1 < 8 and col - 1 >= 0:
        if row_a + 1 == row_d and col_a - 1 == col_d:
            return [row_a + 1, col_a - 1]
    if row_a + 1 < 8 and col + 1 < 8:
        if row_a + 1 == row_d and col_a + 1 == col_d:
            return [row_a + 1, col_a + 1]


matrix = []
for _ in range(8):
    matrix.append(input().split())

white_pawn_coordinates = []
black_pawn_coordinates = []

position_row = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}
positions_col = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

for row in range(8):
    for col in range(8):
        if matrix[row][col] == "w":
            white_pawn_coordinates = [row, col]
        if matrix[row][col] == "b":
            black_pawn_coordinates = [row, col]

for _ in range(8):
    capture_on = check_if_can_capture(white_pawn_coordinates, black_pawn_coordinates)
    if capture_on:
        position = positions_col[capture_on[1]] + position_row[capture_on[0]]
        print(f"Game over! White win, capture on {position}.")
        break

    white_pawn_coordinates[0] -= 1

    if white_pawn_coordinates[0] == 0:
        position = positions_col[white_pawn_coordinates[1]] + position_row[white_pawn_coordinates[0]]
        print(f"Game over! White pawn is promoted to a queen at {position}.")
        break

    capture_on = check_if_can_capture(black_pawn_coordinates, white_pawn_coordinates)
    if capture_on:
        position = positions_col[capture_on[1]] + position_row[capture_on[0]]
        print(f"Game over! Black win, capture on {position}.")
        break

    black_pawn_coordinates[0] += 1

    if black_pawn_coordinates[0] == 7:
        position = positions_col[black_pawn_coordinates[1]] + position_row[black_pawn_coordinates[0]]
        print(f"Game over! Black pawn is promoted to a queen at {position}.")
        break




















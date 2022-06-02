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

def check_if_can_capture(row_w, col_w, row_b, col_b):
    if row_w == row_b - 1 and col_w == col_b - 1:
        return


size = 8
matrix = []


player_w_row = 0
player_w_col = 0
player_b_row = 0
player_b_col = 0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == 'w':
            player_w_row = row
            player_w_col = col
        elif row_elements[col] == 'b':
            player_b_row = row
            player_b_col = col

for _ in range(8):























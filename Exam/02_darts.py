# Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw for each player.
# The score for each turn is deducted from the player’s total score. The first player who reduces their score to zero
# or less wins the game.
# You are going to receive the information for every throw on a separate line. The coordinate information of a hit will
# be in the format: "({row}, {column})".
# •	If a player hits outside the dartboard, he does not score any points.
# •	If a player hits a number, it is deducted from his total.
# •	If a player hits a "D" the sum of the 4 corresponding numbers per column and row is doubled and then deducted from
# his total.
# •	If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled and then deducted from
# his total.
# •	"B" is the bullseye. If a player hits it, he wins the game, and the program ends.
# For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points and they are
# deducted from his total.
# Your job is to find who won the game and with how many turns.
# Input
# •	The name of the first player and the name of the second player, separated by ", "
# •	7 lines – the dartboard (separated by single space)
# •	On the next lines - the coordinates in the format: "({row}, {column})"
# Output
# •	You should print only one line containing the winner and his count of throws:
# "{name} won the game with {count_turns} throws!"


current_player, next_player = input().split(', ')
size = 7
matrix = []

scores = {player: {'trows': 0, 'pts': 501} for player in (current_player, next_player)}


for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

while True:

    row, col = eval(input())
    scores[current_player]['trows'] += 1
    result = 0

    if min(row, col) >= 0 and max(row, col) < 7:
        value = matrix[row][col]
        if value.isnumeric():
            result = int(value)
        elif value == 'D':
            result = 2 * (int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6]))
        elif value == 'T':
            result = 3 * (int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6]))
        elif value == 'B':
            break

    scores[current_player]['pts'] -= result
    if scores[current_player].get('pts') <= 0:
        break
    current_player, next_player = next_player, current_player


winning_trows = scores[current_player].get('trows')
print(f'{current_player} won the game with {winning_trows} throws!')





















# Write a program that reads a number - N, representing the rows and columns of a square matrix. On the next N lines,
# you will receive rows of the matrix. Each row consists of ASCII characters. After that, you will receive a symbol.
# Find the first occurrence of that symbol in the matrix and print i
# ts position in the format: "({row}, {col})". You should start searching from the top left. If there is no such symbol,
# print the message "{symbol} does not occur in the matrix".

n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))
position = None
searched_char = input()

for row_index in range(n):
    for column_index in range(n):
        if searched_char == matrix[row_index][column_index]:
            position = (row_index, column_index)
            print(position)
            break
    if position:
        break
if not position:
    print(f"{searched_char} does not occur in the matrix")

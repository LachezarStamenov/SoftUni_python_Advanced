# Write a program that reads a matrix from the console and prints:
# •	The sum of all matrix elements
# •	The matrix itself
# On the first line, you will get matrix sizes in format "{rows}, {columns}"
rows, cols = [int(el) for el in input().split(', ')]
matrix = []
result = 0
for _ in range(rows):
    nums = [int(el) for el in input().split(', ')]
    result += sum(nums)
    matrix.append(nums)
print(result)
print(matrix)

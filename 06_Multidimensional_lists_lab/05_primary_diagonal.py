# Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right).
# ' On the first line, you will receive an integer N – the size of a square matrix. The next N lines holds the values
# for each column - N numbers, separated by a single space.

n = int(input())
matrix = []

for _ in range(n):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)

diagonal_sum = 0
for index in range(n):
    diagonal_sum += matrix[index][index]
print(diagonal_sum)
# # Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
# On the first line, you will receive an integer N - the size of a square matrix. The following N lines hold the values
# for each column - N numbers separated by a single space. Print the absolute difference between the primary and the
# secondary diagonal sums.
n = int(input())
matrix = []

for _ in range(n):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)
primary_diagonal = []
secondary_diagonal = []

for index in range(n):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][n-1-index])
difference = abs(sum(primary_diagonal)-sum(secondary_diagonal))
print(difference)

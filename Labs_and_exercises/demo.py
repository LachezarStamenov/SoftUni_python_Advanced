def read_matrix():
    rows, cols = [int(x) for x in input().split(', ')]
    matrix = []

    for _ in range(rows):
        nums = [int(el) for el in input().split()]
        matrix.append(nums)

    return matrix

print(read_matrix())
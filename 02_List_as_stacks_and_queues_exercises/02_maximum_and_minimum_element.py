# You have an empty sequence, and you will be given N queries. Each query is one of these three types:
# 1 – Push the element x into the stack.
# 2 – Delete the element present at the top of the stack.
# 3 – Print the maximum element in the stack.
# 4 – Print the minimum element in the stack.
# After you go through all the queries, print the stack in the following format:
# "{n}, {n1}, {n2} …, {nn}"
# Input
# •	The first line of input contains an integer, N
# •	The next N lines each contain an above-mentioned query. (It is guaranteed that each query is valid.)
# Output
# •	For each type 3 or 4 query, print the maximum/minimum element in the stack on a new line
# Constraints
# •	1 ≤ N ≤ 105
# •	1 ≤ x ≤ 109
# •	1 ≤ type ≤ 4

n = int(input())
stack = []

for _ in range(n):
    line_parts = input().split()
    command = line_parts[0]

    if command == '1':
        number = int(line_parts[1])
        stack.append(number)
    elif command == '2' and stack:
        stack.pop()
    elif command == '3' and stack:
        print(max(stack))
    elif command == '4' and stack:
        print(min(stack))
while stack:
    el = stack.pop()
    if stack:
        print(el, end=', ')
    else:
        print(el)
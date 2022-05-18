# Write a program that reads N integers from the console and reverses them using a stack

line = input().split()

while line:
    print(f"{line.pop()}", end=' ')
# Hot potato is a game in which children form a circle and start passing a hot potato. The counting starts with the
# first kid. Every nth toss the child left with the potato leaves the game. When a kid leaves the game, it passes the
# potato along. This continues until there is only one kid left.
# Create a program that simulates the game of Hot Potato. Print every kid that is removed from the circle. In the end,
# print the kid that is left last.
from collections import deque

kids = deque(input().split())
n = int(input())

while len(kids) > 1:
    kids.rotate(-n)
    print(f"Removed {kids.pop()}")

print(f"Last is {kids.popleft()}")
# Write a program that reads an input consisting of a name and adds it to a queue until "End" is received. If you
# receive "Paid", print every customer name and empty the queue, otherwise we receive a client and we must add him
# to the queue. When we receive "End", we must print the count of the remaining people in the queue in the format:
# "{count} people remaining."
from collections import deque

name = input()
line = deque()

while not name == "End":
    if name == "Paid":
        while line:
            print(line.popleft())
    else:
        line.append(name)
    name = input()
print(f"{len(line)} people remaining.")
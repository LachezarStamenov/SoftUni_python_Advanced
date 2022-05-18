# Write a program to flatten several lists of numbers received in the following format:
# 	String with numbers or empty strings separated by "|"
# 	Values are separated by spaces (" ", one or several)
# 	Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below
from collections import deque

sub_lists = input().split('|')

result = []

while sub_lists:
    sublist = sub_lists.pop().split() # split remove all spaces
    for el in sublist:
        result.append(el)
print(*result, sep=' ')





# You own a fashion boutique and you receive a delivery once a month in a huge box, which is full of clothes.
# You must arrange them in your store, so you take the box and start from the last piece of clothing on the top of
# the pile to the first one at the bottom. Use a stack for the purpose. Each piece of clothing has its value
# (an integer). You must sum their values, while you take them out of the box. You will be given an integer
# representing the capacity of a rack. While the sum of the clothes is less than the capacity, keep summing them.
# If the sum becomes equal to the capacity you must take a new rack for the next clothes, if there are any left in the
# box. If it becomes greater than the capacity, don't add the piece of clothing to the current rack and take a new one.
# In the end, print how many racks you have used to hang must the clothes.
# Input
# •	On the first line you will be given a sequence of integers, representing the clothes in the box, separated by a
# single space.
# •	On the second line, you will be given an integer, representing the capacity of a rack.
# Output
# •	Print the number of racks, needed to hang must the clothes from the box.
# Constraints
# •	The values of the clothes will be integers in the range [0,20]
# •	There will never be more than 50 clothes in a box
# •	The capacity will be an integer in the range [0,20]
# •	None of the integers from the box will be greater than then the value of the capacity
clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

used_racks = 1
current_rack = rack_capacity

while clothes:
    current_piece = clothes[-1]  # peek of stack

    if current_piece <= current_rack:
        clothes.pop()
        current_rack -= current_piece
    else:
        used_racks += 1
        current_rack = rack_capacity

print(used_racks)


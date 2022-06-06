# Aladdin, rich and powerful with the help of the Genie, is now preparing to marry the princess Jasmine. He asks Genie
# for help to prepare the wedding presents.
# First, you will receive a sequence of integers representing the materials for every wedding present. After that, you
# will be given another sequence of integers – Genie magic level for every aim to make a gift.
# Your task is to mix materials with magic levels so you can make presents, listed in the table below.
# Gift	Magic needed
# Gemstone	100 to 199
# Porcelain Sculpture	200 to 299
# Gold	300 to 399
# Diamond Jewellery	400 to 499
#
# To make a present, you should take the last integer of materials and sum it with the first magic level value. If the
# result is between or equal to the numbers described in the table above, you make the corresponding gift and remove
# both materials and magic value. Otherwise:
# •	If the product of the operation is under 100:
# o	And if it is an even number, double the materials, and triple the magic, then sum it again.
# o	And if it is an odd number, double the sum of the materials and the magic level. Then, check again if it is between
# or equal to any of the numbers in the table above.
# •	If the product of the operation is more than 499, divide the sum of the material and the magic level by 2. Then,
# check again if it is between or equal to any of the numbers in the table above.
# •	If, however, the result is not between or equal to any of the numbers in the table above after performing the
# calculation, remove both the materials and the magic level.
# Stop crafting gifts when you are out of materials or magic level.
# You have succeeded in crafting the presents when you've crafted either one of the pairs - a gemstone and a sculpture
# or gold and jewellery.
# Input
# •	The first line of input will represent the values of materials - integers, separated by a single space
# •	On the second line, you will be given the magic levels - integers, separated by a single space
# Output
# •	On the first line - print whether you have succeeded in crafting the presents:
# o	"The wedding presents are made!"
# o	"Aladdin does not have enough wedding presents."
# •	On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:
# o	"Materials left: {material1}, {material2}, …"
# o	"Magic left: {magicValue1}, {magicValue2}, …
# •	On the next lines, print the gifts alphabetically that the Genie has crafted at least once:
# "{present1}: {amount}
# {present2}: {amount}
# …
# {presentN}: {amount}"
# Constraints
# •	All the materials values will be integers in the range [1, 1000]
# •	Magic level values will be integers in the range [1, 1000]
from collections import deque


def check_for_gift(total_sum, gifts):
    result = total_sum
    if 100 <= result <= 199:
        gifts['Gemstone'] += 1
    elif 200 <= result <= 299:
        gifts['Porcelain Sculpture'] += 1
    elif 300 <= result <= 399:
        gifts['Gold'] += 1
    elif 400 <= result <= 499:
        gifts['Diamond Jewellery'] += 1
    return gifts

def check_for_succeeded_crafting(gifts):
    if gifts['Gemstone'] > 0 and gifts['Porcelain Sculpture'] > 0:
        return True
    elif gifts['Gold'] > 0 and gifts['Diamond Jewellery'] > 0:
        return True
    else:
        return False


materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

gifts = {'Gemstone': 0, 'Porcelain Sculpture': 0, 'Gold': 0, 'Diamond Jewellery': 0}

while True:
    if not materials or not magic_levels:
        break

    current_material = materials.pop()
    current_magic_level = magic_levels.popleft()
    total_sum = current_material + current_magic_level

    if total_sum < 100 and total_sum % 2 == 0:
        total_sum = current_material * 2 + current_magic_level * 3
        if total_sum < 100 or total_sum > 499:
            continue
        else:
            check_for_gift(total_sum,  gifts)

    elif total_sum < 100 and total_sum % 2 != 0:
        total_sum *= 2
        if total_sum < 100 or total_sum > 499:
            continue
        else:
            check_for_gift(total_sum, gifts)
    elif total_sum > 499:
        total_sum /= 2
        if total_sum < 100 or total_sum > 499:
            continue
        else:
            check_for_gift(total_sum, gifts)

    else:
        check_for_gift(total_sum, gifts)

if check_for_succeeded_crafting(gifts):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

sorted_gifts = dict(x for x in (sorted(gifts.items(), key=lambda x: x[0])) if x[1] > 0)
for key, value in sorted_gifts.items():
    print(f"{key}: {value}")
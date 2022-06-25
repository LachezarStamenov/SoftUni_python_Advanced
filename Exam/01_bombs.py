# You will be given two sequences of integers, representing bomb effects and bomb casings.
# You need to start from the first bomb effect and try to mix it with the last bomb casing. If the sum of their values
# is equal to any of the materials in the table below – create the bomb corresponding to the value and remove both bomb
# materials. Otherwise, just decrease the value of the bomb casing by 5. You need to stop combining when you have no
# more bomb effects or bomb casings, or you successfully filled the bombs pouch.
# Bombs:
# •	Datura Bombs: 40
# •	Cherry Bombs: 60
# •	Smoke Decoy Bombs: 120
# To fill the bomb pouch, Ezio needs three of each of the bomb types.
# Input
# •	On the first line, you will receive the integers representing the bomb effects, separated by ", ".
# •	On the second line, you will receive the integers representing the bomb casings, separated by ", ".
# Output
# •	On the first line, print:
# o	if Ezio succeeded to fulfill the bomb pouch: "Bene! You have successfully filled the bomb pouch!"
# o	if Ezio didn't succeed to fulfill the bomb pouch: "You don't have enough materials to fill the bomb pouch."
# •	On the second line, print all bomb effects left:
# o	If there are no bomb effects: "Bomb Effects: empty"
# o	If there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"
# •	On the third line, print all bomb casings left:
# o	If there are no bomb casings: "Bomb Casings: empty"
# o	If there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"
# •	Then, you need to print all bombs and the count you have of them, ordered alphabetically:
# o	"Cherry Bombs: {count}"
# o	"Datura Bombs: {count}"
# o	"Smoke Decoy Bombs: {count}"
# Constraints
# •	All of the given numbers will be valid integers in the range [0, 120].
# •	There will be no cases with negative material.
from collections import deque

bombs_effect = deque(int(x) for x in input().split(', '))
bombs_casings = [int(x) for x in input().split(', ')]

bombs_types = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}
bombs_made = {'Cherry Bombs': 0, 'Datura Bombs': 0, 'Smoke Decoy Bombs': 0}

is_bombs_list_filled = False


while bombs_effect and bombs_casings:
    if bombs_made['Cherry Bombs'] >= 3 \
                           and bombs_made['Datura Bombs'] >= 3 \
                           and bombs_made['Smoke Decoy Bombs'] >= 3:
        is_bombs_list_filled = True
        break

    current_effect = bombs_effect.popleft()
    current_causing = bombs_casings.pop()
    sum_value = current_effect + current_causing

    if sum_value in bombs_types.keys():
        bombs_made[bombs_types[sum_value]] += 1
    else:
        bombs_casings.append(current_causing - 5)
        bombs_effect.appendleft(current_effect)

if is_bombs_list_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bombs_effect:
    print(f"Bomb Effects: {', '.join(str(x) for x in bombs_effect)}")
else:
    print("Bomb Effects: empty")

if bombs_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bombs_casings)}")
else:
    print("Bomb Casings: empty")

for key, value in bombs_made.items():
    print(f"{key}: {value}")

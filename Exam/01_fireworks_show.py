# First, you will be given a sequence of integers representing firework effects. Afterwards you will be given another
# sequence of integers representing explosive power.
# You need to start from the first firework effect and try to mix it with the last explosive power. If the sum of their
# values is:
# •	divisible by 3, but it is not divisible by 5 – create Palm firework and remove both materials
# •	divisible by 5, but it is not divisible by 3 – create Willow firework and remove both materials
# •	divisible by both 3 and 5 – create Crossette firework and remove both materials
# Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence. Then, try to mix
# the same explosive power with the next firework effect.
# If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other.
# When you have successfully prepared enough fireworks for the show or you have no more firework punches or explosive
# power, you need to stop mixing.
# To make the perfect firework show, Maria needs 3 of each of the firework types.
# Input
# •	On the first line, you will receive the integers representing the firework effects, separated by ", ".
# •	On the second line, you will receive the integers representing the explosive power, separated by ", ".
# Output
# •	On the first line, print:
# o	if Maria successfully prepared the firework show: "Congrats! You made the perfect firework show!"
# o	if Maria failed to prepare it: "Sorry. You can't make the perfect firework show."
# •	On the second line, print all firework effects left if there are any:
# o	"Firework Effects left: {effect1}, {effect2}, (…)"
# •	On the third line, print all explosive fillings left if there are any:
# o	" Explosive Power left: {filling1}, {filling2}, (…)"
# •	Then, you need to print all fireworks and the amount you have of them:
# o	"Palm Fireworks: {count}"
# o	"Willow Fireworks: {count}"
# o	"Crossette Fireworks: {count}"
# Constraints
# •	All the given numbers will be integers in the range [-100, 100].
# •	There will be no cases with empty sequences.


from collections import deque

firework_effects = deque([int(x) for x in input().split(', ')])
explosive_power = [int(x) for x in input().split(', ')]

is_perfect_show = False

fireworks = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}

while True:

    if fireworks['Palm Fireworks'] >= 3 and fireworks['Willow Fireworks'] >= 3 and fireworks['Crossette Fireworks'] >= 3:
        is_perfect_show = True
        break
    if not firework_effects or not explosive_power:
        break
    current_effect = firework_effects.popleft()
    if current_effect <= 0:
        continue

    current_power = explosive_power.pop()
    if current_power <= 0:
        firework_effects.appendleft(current_effect)
        continue

    mix = current_effect + current_power

    if mix % 3 == 0 and mix % 5 != 0:
        fireworks['Palm Fireworks'] += 1
    elif mix % 5 == 0 and mix % 3 != 0:
        fireworks['Willow Fireworks'] += 1
    elif mix % 3 == 0 and mix % 5 == 0:
        fireworks['Crossette Fireworks'] += 1
    else:
        current_effect -= 1
        firework_effects.append(current_effect)
        explosive_power.append(current_power)

if is_perfect_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")
for key, value in fireworks.items():
    print(f"{key}: {value}")
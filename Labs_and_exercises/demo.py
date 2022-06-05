from collections import deque

elfs_energies = deque(int(x) for x in input().split())
materials = [int(x) for x in input().split()]

toys = 0
consumed_energy = 0
elves_count = 0

while True:
    if not materials or not elfs_energies:
        break

    current_energy = elfs_energies.popleft()
    current_material = materials.pop()

    if current_energy < 5:
        materials.append(current_material)
        continue

    needed_energy = current_material
    elves_count += 1

    if elves_count % 3 == 0:
        needed_energy = current_material * 2

    if current_energy < needed_energy:
        elfs_energies.append(current_energy * 2)
        materials.append(current_material)
        continue

    consumed_energy += needed_energy
    current_energy -= needed_energy

    if elves_count % 3 == 0:
        if elves_count % 5 == 0:
            elfs_energies.append(current_energy)
        else:
            elfs_energies.append(current_energy + 1)
            toys += 2

    elif elves_count % 5 == 0:
        elfs_energies.append(current_energy)

    else:
        elfs_energies.append(current_energy + 1)
        toys += 1



print(f"Toys: {toys}")
print(f"Energy: {consumed_energy}")
if elfs_energies:
    print(f"Elves left: {' '.join(str(x) for x in elfs_energies)}")
if materials:
    print(f"Boxes left: {materials}")

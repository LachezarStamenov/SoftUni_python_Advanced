# Write a program that reads on the first line the starting quantity of water in a dispenser. Then on the next few lines
# you will be given the names of some people that want to get water (each on separate line) until you receive the
# command "Start". Add those people in a queue. Finally, you will receive some commands until the command "End":
# -	{liters} - Litters that the current person in the queue wants to get. Check if there is enough water in the
# dispenser for that person.
# o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
# o	Otherwise, print "{person} must wait" and remove the person from the queue without reducing the water in the
# dispenser
# -	refill {liters} - add the given litters in the dispenser.
# At the end print how many litters of water are left in the format: "{left_liters} liters left"


from collections import deque

water_quantity = int(input())
line = deque()
name = input()

while not name == "Start":
    line.append(name)
    name = input()
command = input()

while not command == "End":
    if command.isdigit():
        required_liters = int(command)
        name = line.popleft()
        if water_quantity >= required_liters:
            water_quantity -= required_liters
            print(f"{name} got water")
        else:
            print(f"{name} must wait")
    else:
        _, liters_to_fill = command.split()
        liters_to_fill = int(liters_to_fill)
        water_quantity += liters_to_fill

    command = input()
print(f"{water_quantity} liters left")
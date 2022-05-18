# Write a program that:
# •	Records a car number for every car that enters the parking lot
# •	Removes a car number when the car leaves the parking lot
# The input will be the number of commands, which you will receive, and cars in the format: direction, car_number.
# Print the car numbers, which are still in the parking lot.
# NOTE: The order in which we print the result does not matter.

n = int(input())
cars = set()

for _ in range(n):
    direction, car_number = input().split(", ")
    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT":
        cars.remove(car_number)
if cars:
    print('\n'.join(cars))
else:
    print("Parking Lot is Empty")
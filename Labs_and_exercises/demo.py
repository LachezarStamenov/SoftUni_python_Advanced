from collections import deque

green0 = int(input())
free_window0 = int(input())
cars_passed = 0
car_lenght = 0
list_cars = deque()
hit = 'no'

command0 = input()

while command0 != "END":
    list_cars.append(command0)
    command0 = input()

green = green0
free_window = free_window0

while list_cars:
    next_car = list_cars.popleft()
    if next_car != 'green':
        car_lenght = len(next_car)
        if green == 0:
            break

        elif green >= car_lenght:
            green -= car_lenght
            cars_passed += 1

        else:
            free_window -= (car_lenght - green)
            green = 0
            if free_window >= 0:
                cars_passed += 1

            else:
                print("A crash happened!")
                letter = next_car[free_window:]
                letter = letter[:1]
                hit = 'yes'
                print(f'{next_car} was hit at {letter}.')
                break

    else:
        green = green0
        free_window = free_window0

if hit == 'no':
    print('Everyone is safe.')
    print(f'{cars_passed} total cars passed the crossroads.')
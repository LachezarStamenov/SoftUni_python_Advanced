# Somewhere in the future, there is a robotics factory. The current project is assembly line robots.
# Each robot has a processing time, the time it needs to process a product. When a robot is free it should take a
# product for processing and log his name, product and processing start time.
# Each robot processes a product coming from the assembly line. A product is coming from the line each second (so the
# first product should appear at [start time + 1 second]). If a product passes the line and there is not a free robot
# to take it, it should be queued at the end of the line again.
# The robots are standing on the line in the order of their appearance.
# Input
# •	On the first line, you will get the names of the robots and their processing times in format "robotName-processTime
# ;robotName-processTime;robotName-processTime"
# •	On the second line, you will get the starting time in format "hh:mm:ss"
# •	Next, until the "End" command, you will get a product on each line.
from collections import deque


def convert_str_to_seconds(str_time):
    hours, minutes, seconds = [int(x) for x in str_time.split(':')]
    return hours * 60 * 60 + minutes * 60 + seconds


def convert_sec_to_str_time(seconds):
    seconds %= 24 * 60 * 60      # this check if the day finished and pass to next day
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)


robots_data = input().split(';')
process_time_by_robot = {}
busy_until_by_robot = {}

for robot_data in robots_data:
    name, process_time = robot_data.split('-')
    process_time_by_robot[name] = int(process_time)
    busy_until_by_robot[name] = -1

time = convert_str_to_seconds(input())
items = deque()

while True:
    line = input()
    if line == 'End':
        break
    items.append(line)

while items:
    time += 1
    item = items.popleft()

    for name, busy_until in busy_until_by_robot.items():
        if time >= busy_until:
            busy_until_by_robot[name] = time + process_time_by_robot[name]
            print(f'{name} - {item} [{convert_sec_to_str_time(time)}]')
            break
    else:
        items.append(item)

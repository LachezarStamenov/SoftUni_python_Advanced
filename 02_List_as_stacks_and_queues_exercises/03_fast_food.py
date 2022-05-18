# You have a fast food restaurant and most of the food that you're offering is previously prepared. You need to know
# if you will have enough food to serve lunch to all your customers.
# Write a program that checks the orders' quantity. You also want to know the client with the biggest order for the
# day, because you want to give him a discount the next time he comes.
# First, you will be given the quantity of the food that you have for the day (an integer number). Next, you will be
# given a sequence of integers, each representing the quantity of an order. Keep the orders in a queue. Find the biggest
# order and print it. You will begin servicing your clients from the first one that came. Before you serve the next
# order, you should check if you have enough food left to complete it. If you have, remove the order from the queue
# and reduce the amount of food you have. If you do not – do not serve any other customer and end the program.
# If you succeeded in servicing all your clients, print:
# "Orders complete".
#  If not, print:
# "Orders left: {order1} {order2} .... {orderN}".
# Input
# •	On the first line you will be given the quantity of your food - an integer in the range [0, 1000]
# •	On the second line you will receive a sequence of integers, representing each order, separated by a single space
# Output
# •	Print the quantity of biggest order

from collections import deque

total_amount_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))
while orders:
    current_order = orders[0]
    if current_order > total_amount_food:
        break
    total_amount_food -= current_order
    orders.popleft()
if not orders:
    print("Orders complete")
else:
    print(f'Orders left: {" ".join([str(x) for x in orders])}')


from collections import deque

bowels = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while True:
    if not bowels or not customers:
        break
    else:
        current_ramen = bowels.pop()
        current_customer = customers.popleft()
        if current_ramen == current_customer:
            continue
        elif current_ramen > current_customer:
            current_ramen -= current_customer
            bowels.append(current_ramen)
        elif current_ramen < current_customer:
            current_customer -= current_ramen
            customers.appendleft(current_customer)
if not customers:
    print("Great job! You served all the customers.")
    if bowels:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowels)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
# Write a function called multiply that can receive any quantity of numbers (integers) as different parameters and
# returns the result of the multiplication of all of them. Submit only your function in the Judge system.A

def multiply(*args):
    result = 1
    for el in args:
        result *= el
    return result

print(multiply(1, 4 ,5))
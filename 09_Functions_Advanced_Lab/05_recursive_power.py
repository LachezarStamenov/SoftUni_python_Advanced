# Create a recursive function called recursive_power() which should receive a number and a power. Using recursion,
# return the result of number ** power. Submit only the function in the judge system.

def recursive_power(number: int, power: int):
    output = number
    if power > 1:
        output *= recursive_power(number, power - 1)

    return output


print(recursive_power(2, 10))
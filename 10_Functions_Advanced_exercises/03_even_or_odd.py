# Create a function called even_odd() that can receive a different quantity of numbers and a command at the end. The
# command can be "even" or "odd". Filter the numbers depending on the command and return them in a list. Submit only
# the function in the judge system.

def even_odd(*args):
    if args[-1] == 'even':
        even_nums = [x for x in args[:-1] if x % 2 == 0]
        return even_nums
    elif args[-1] == "odd":
        odd_nums = [x for x in args[:-1] if x % 2 != 0]
        return odd_nums

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

# Write a function called numbers_searching which receives a different amount of parameters. All parameters will be
# integer numbers forming a sequence of consecutive numbers. Your task is to find an unknown amount of duplicates from
# the given sequence and a missing value, such that all the duplicate values and the missing value are between the
# smallest and the biggest received number.
# The function should return a list with the last missing number as a first argument and a sorted list, containing the
# duplicates found, in ascending order.
# For example: if we have the following numbers: 1, 2, 4, 2, 5, 4 will return 3 as missing number and 2, 4 as duplicate
# numbers in the following format: [3, [2, 4]]
# Input
# •	There will be no input
# •	Parameters will be passed to your function
# Output
# •	The function should return a list in the following format: [missing number, [duplicate_numbers separated with comma
# and space]]
# Constraints
# •	The missing number will always be between the smallest and the biggest received number

def numbers_searching(*args):
    args = sorted(args)
    missing_value = [num for num in range(args[0], args[-1]+1) if num not in args]
    unique_numbers = []
    duplicate_numbers = []
    for i in args:
        if i not in unique_numbers:
            unique_numbers.append(i)
        else:
            if i in duplicate_numbers:
                continue
            else:
                duplicate_numbers.append(i)
    missing_value.append(duplicate_numbers)
    return missing_value


print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
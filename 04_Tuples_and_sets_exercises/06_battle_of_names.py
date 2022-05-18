# You will receive a number N. On the next N lines, you will be receiving names. You must sum the ASCII values of
# each letter in the name and integer divide it to the number of the current row (starting from 1). Save the result
# to a set of either odd or even numbers, depending on if the devised number is an odd or even. After that, sum the
# values of each set.
# •	If the sums of the two sets are equal, print the union values, separated by ", ".
# •	If the sum of the odd numbers is larger than the sum of the even numbers, print the different values, separated
# by ", ".
# •	If the sum of the even numbers is larger than the sum of the odd numbers, print the symmetric different values,
# separated by ", ".
# NOTE: On every operation, the starting set should be the odd set

n = int(input())

odd_set = set()
even_set = set()

even_sum = 0
odd_sum = 0

for row in range(1, n + 1):
    name_sum = sum([ord(x) for x in input()]) // row
    if name_sum % 2 == 0:
        even_set.add(name_sum)
        even_sum += name_sum
    else:
        odd_set.add(name_sum)
        odd_sum += name_sum

if even_sum == odd_sum:
    result = odd_set.union(even_set)
elif even_sum > odd_sum:
    result = odd_set.symmetric_difference(even_set)
else:
    result = odd_set.difference(even_set)
print(*result, sep=', ')

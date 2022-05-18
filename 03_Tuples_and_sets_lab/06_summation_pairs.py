# On the first line, you will receive a string of numbers separated by space. On the second line, you'll receive a
# target number. Your task is to find all pairs of numbers whose sum equals the target number.
# For each found pair print "{number} + {number} = {target_number}".
# Then, save only the unique pairs. Note: (1, 2) and (2, 1) are unique.
# Also, you should keep track of how many iterations you've done.
# At the end print all the iterations done in format: "Iterations done: {total_number_of_iterations}".
# On the following lines, print the unique pairs in the format: "(first_number, second_number)".
# The order in which we print the result does not matter.

line = [int(x) for x in input().split()]
sum_target = int(input())
n = len(line)
iterations = 0
unique_pairs = set()


for i in range(0, n):
    for j in range(i + 1, n):
        if line[i] + line[j] == sum_target:
            print(f'{line[i]} + {line[j]} = {sum_target}')
            unique_pairs.add((line[i], line[j]))
        iterations += 1
print(f'Iterations done: {iterations}')
for pair in unique_pairs:
    print(pair)


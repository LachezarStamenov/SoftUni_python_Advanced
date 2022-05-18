# Write a program that finds the longest intersection. You will be given a number N. On the next N lines you will be
# given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". Find the intersection of
# these two ranges and save the longest one of all N intersections. At the end print the numbers that are included in
# the longest intersection and its length in the format: "Longest intersection is {longest_intersection} with length
# {length_longest_intersection}"
# Note: in each range, there will always be intersection. If there are two equal intersections, print the first one.

def generate_seq(range_info):
    start, end = [int(x) for x in range_info.split(',')]
    return set(range(start, end + 1))


n = int(input())
longest_intersection = set()

for _ in range(n):
    line_parts = input().split('-')
    first_set = generate_seq(line_parts[0])
    second_set = generate_seq(line_parts[1])
    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is [{', '.join([str(x) for x in longest_intersection])}] with length "
      f"{len(longest_intersection)}")


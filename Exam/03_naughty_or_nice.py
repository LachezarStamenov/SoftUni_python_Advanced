# Write a function called naughty_or_nice_list which will receive
# •	A list representing Santa Claus' "Naughty or Nice" list full of kids' names
# •	A different number of arguments (strings) and/or keywords representing commands
# The function should sort the kids in the given Santa Claus list into 3 lists: "Nice", "Naughty", and "Not found".
# The list holds a different number of kids - tuples containing two elements: a counting number (integer) at the first
# position and a name (string) at the second position.
# For example: [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")].
# Next, the function could receive arguments and/or keywords.
# Each argument is a command. The commands could be the following:
# •	"{counting_number}-Naughty" - if there is only one tuple in the given list with the same number, MOVE the kid to a
# list with NAUGHTY kids and remove it from the Santa list. Otherwise, ignore the command.
# •	"{counting_number}-Nice" - if there is only one tuple in the given list with the same number, MOVE the kid to a
# list with NICE kids and remove it from the Santa list. Otherwise, ignore the command.
# Each keyword holds a key with a name (string), and each value will be a string ("Naughty" or "Nice"):
# •	If there is only one tuple with the same name, MOVE the kid to a list with NAUGHTY or to the list with NICE kids
# depending on the value in the keyword. Then, remove it from the Santa list.
# •	Otherwise, ignore the command.
# All remaining tuples in the given Santa's list are not found kids, and they should be MOVED to the "Not found" list.
# In the end, return the final lists, each on a new line as described below.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input. Just parameters passed to your function.
# Output
# •	The function should return strings with the names on each list on separate lines, if there are any, otherwise
# skip the line:
# 	"Nice: {name1}, {name2} … {nameN}"
# 	"Naughty: {name1}, {name2} … {nameN}"
#   "Not found: {name1}, {name2} … {nameN}"
from collections import Counter

def naughty_or_nice_list(names_list,*args, **kwargs):
    lists = {'Naughty': [], 'Nice':  [], 'Not found': []}
    num_counter = Counter(el[0] for el in names_list)

    for pair in args:
        counting_num = int(pair.split('-')[0])
        list_name = pair.split('-')[1]
        if num_counter[counting_num] == 1:
            name = [name for num, name in names_list if num == counting_num]
            lists[list_name].extend(name)
            names_list = [el for el in names_list if el[0] != counting_num]
    name_counter = Counter(el[1] for el in names_list)

    for name, type in kwargs.items():
        if name_counter[name] == 1:
            lists[type].append(name)
            names_list = [el for el in names_list if el[1] != name]

    for num, name in names_list:
        lists["Not found"].append(name)

    output = ""

    for type, kids in lists.items():
        if kids:
            output += f"{type}: {', '.join(kids)}\n"

    return output


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))



#
# from collections import Counter
#
#
# def naughty_or_nice_list(names_list,*args, **kwargs):
#     santa_list = {"Nice":[], "Naughty": [], "Not found": []}
#     num_counter = Counter(el[0] for el in names_list)
#
#     for el in args:
#         data = el.split("-")
#         number = int(data[0])
#         kid_type = data[1]
#         if num_counter[number] == 1:
#             name = [name for num, name in names_list if num == number]
#             santa_list[kid_type].extend(name)
#             names_list = [el for el in names_list if el[0] != number]
#
#     name_counter = Counter(el[1] for el in names_list)
#
#     for name, type in kwargs.items():
#         if name_counter[name] == 1:
#             santa_list[type].append(name)
#             names_list = [el for el in names_list if el[1] != name]
#
#     for num, name in names_list:
#         santa_list["Not found"].append(name)
#
#     output = ""
#
#     for type, kids in santa_list.items():
#         if kids:
#             output += f"{type}: {', '.join(kids)}\n"
#
#     return output
#
# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))
















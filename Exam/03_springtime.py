# Spring is the season of new beginnings. Fresh buds bloom, animals awaken and the earth seems to come to life again.
# Farmers and gardeners plant their seeds and temperatures slowly rise.
# Write a function called start_spring which will receive a different number of keyword arguments.
# Each keyword holds a key with a name of the spring object (string), and each value holds its type (string). For
# example, dahlia="flower", shrikes="bird", dogwood="tree".
# The function should sort the given spring objects in collections by their type:
# •	The collections sorted by their number of elements in descending order. If two or more collections have the same
# number of elements in them, return them in ascending order (alphabetically) by the type's name.
# •	Each collection's elements should be sorted in ascending order (alphabetically) by the object's name.
#
# Input
# •	There will be no input. Just parameters passed to your function.
# Output
# •	Return the result, sorted as described above in the format:
# o	"{type_one}:
# -{spring_object_of_this_type_one}
# -{spring_object_of_this_type_two}
# …
# -{spring_object_of_this_type_N}
# {type_two}:
# …
# {type_N}:
# …
# -{last_spring_object_of_typeN}"

def start_spring(**kwargs):
    collection = {}
    result = ""
    for key, value in kwargs.items():
        if value not in collection:
            collection[value] = []
        collection[value].append(key)

    sorted_collection = dict(sorted(collection.items(), key=lambda x: (-len(x[1]), x[0])))
    for key, value in sorted_collection.items():
        result += f'{key}:\n'
        for type_obj in sorted(value):
            result += f'-{type_obj}\n'
    return result




example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))



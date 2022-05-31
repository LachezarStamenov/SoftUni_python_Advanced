# Create a function called age_assignment() that receives a different number of names and a different number of
# key-value pairs. The key will be a single letter (the first letter of each name) and the value - a number (age).
# Find its first letter in the key-value pairs for each name and assign the age to the person's name.
# Then, sort the names in ascending order (alphabetically) and return the information for each person on a new line in
# the format: "{name} is {age} years old."
def age_assignment(*args, **kwargs):
    result = {}

    for name in args:
        first_letter = name[0]
        age = kwargs[first_letter]
        result[name] = age
    sorted_result = [f'{key} is {value} years old.' for key, value in sorted(result.items(), key=lambda x: x[0])]

    return '\n'.join(sorted_result)

print(age_assignment("Peter", "George", G=26, P=19))
# Create a function called func_executor() that can receive a different number of tuples, each of which will have
# exactly 2 elements: the first will be a function, and the second will be a tuple of the arguments that need to be
# passed to that function. You should execute each function and return its result in the format:
# "{function name} - {function result}"
# For more clarification, see the examples below.

def func_executor(*args):
    result = []
    for arg in args:
        func_ref, func_params = arg
        func_result = func_ref(*func_params)
        result.append(f'{func_ref.__name__} - {func_result}')
    return '\n'.join(result)


def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))


# We are given an arithmetic expression with brackets. Scan through the string and extract each sub-expression.
# Print the result back on the console

expression = input()

par_stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        par_stack.append(index)
    elif expression[index] == ")":
        start_index = par_stack.pop()
        print(expression[start_index: index + 1])




# You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced.
# A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs
# after the former. There will be no interval symbols between the parentheses. You will be given three types of
# parentheses: (, {, and [.
# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.
# Input
# •	Each input consists of a single line, the sequence of parentheses.
# Output
# •	For each test case, print on a new line "YES" if the parentheses are balanced.
# Otherwise, print "NO". Do not print the quotes.
# Constraints
# •	1 ≤ lens ≤ 1000, where lens is the length of the sequence.
# •	Each character of the sequence will be one of {, }, (, ), [, ].

string = input()

opening_brackets = []

balanced = True

for ch in string:
    if ch in '([{':
        opening_brackets.append(ch)
    elif not opening_brackets:
        balanced = False
    else:
        last_opening_brackets = opening_brackets.pop()
        if f'{last_opening_brackets}{ch}' not in '()[]{}':
            balanced = False
            break

if balanced and not opening_brackets:
    print('YES')
else:
    print('NO')

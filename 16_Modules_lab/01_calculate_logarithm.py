# Write a program that prints the calculated logarithm of any given number
# Input
# •	On the first line, you will receive the number (an integer)
# •	On the second line, you will receive a number, which is the logarithm base. It can be either a number or the word
# "natural"
# The output should be formatted to the 2nd decimal digit


from math import log, e

# Log(b)X = Y => B^y = X
# Log)2)1024 = 10 => 2 ^ 10 = 1024

value = int(input())
base = input()

if base == 'natural':
    result = log(value, e)
else:
    result = log(value, int(base))
print(f"{result:.2f}")

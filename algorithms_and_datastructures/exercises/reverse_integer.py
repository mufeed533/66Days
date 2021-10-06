"""
Reverse an integer input
"""
from functools import reduce


def reverse_string(string):
    return reduce(lambda x, y: y + x, string)


def reverse_integer_1(integer):
    reversed_integer = int(reverse_string(str(abs(integer))))
    if integer < 0:
        reversed_integer = int(reversed_integer) * -1
    return reversed_integer


integer_input = int(input())
print(reverse_integer_1(integer_input))
# print(reverse_integer_2(integer_input))

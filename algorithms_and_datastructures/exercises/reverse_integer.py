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


def reverse_integer_2(integer):
    reversed_integer = 0
    is_negative = 1 if integer > 0 else -1
    integer = abs(integer)
    while integer >= 1:
        reversed_integer = reversed_integer * 10 + integer % 10
        integer = integer // 10
    return reversed_integer * is_negative


integer_input = int(input())
print(reverse_integer_1(integer_input))
print(reverse_integer_2(integer_input))

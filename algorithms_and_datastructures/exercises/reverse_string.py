"""
Reverse an input string
"""
from functools import reduce


def reverse_1(string):
    output_string = ""
    for i in range(len(string) - 1, -1, -1):
        output_string += string[i]
    return output_string



def reverse_2(string):
    string = "".join(reversed(string))
    return string


def reverse_3(string):
    return string[::-1]


def reverse_4(string):
    output_string = ""
    for i in string:
        output_string = i + output_string
    return output_string


def reverse_5(string):
    return reduce((lambda x, y: y + x), string)


input_string = str(input())
print(reverse_1(input_string))
print(reverse_2(input_string))
print(reverse_3(input_string))
print(reverse_4(input_string))
print(reverse_5(input_string))

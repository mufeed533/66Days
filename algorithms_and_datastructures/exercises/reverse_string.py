"""
Reverse an input string
"""


def reverse_1(string):
    output_string = ""
    for i in range(len(string) - 1, -1, -1):
        output_string += string[i]
    return output_string


def reverse_2(string):
    string = "".join(reversed(string))
    return string


input_string = str(input())
print(reverse_1(input_string))
print(reverse_2(input_string))

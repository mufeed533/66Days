"""
Reverse an input string
"""


def reverse(string):
    output_string = ""
    for i in range(len(string) - 1, -1, -1):
        output_string += string[i]
    return output_string


input_string = str(input())
print(reverse(input_string))

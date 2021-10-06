"""
Check if an input string is palindrome or not
"""
from functools import reduce


def is_palindrome_1(string):
    reversed_string = reduce(lambda x, y: y + x, string)
    return reversed_string == string


input_string = str(input())
print(is_palindrome_1(input_string))

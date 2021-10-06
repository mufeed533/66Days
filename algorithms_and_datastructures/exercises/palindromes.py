"""
Check if an input string is palindrome or not
"""
from functools import reduce


def is_palindrome(string):
    reversed_string = reduce(lambda x, y: y + x, string)
    return True if reversed_string == string else False


input_string = str(input())
print(is_palindrome(input_string))

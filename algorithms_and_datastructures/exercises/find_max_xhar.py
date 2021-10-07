"""
Find the character that is most occurring in a string
"""
from collections import Counter


def find_max_char_1(string):
    char_map = Counter(string)
    print(char_map)
    largest_string = []
    largest_string_occurrence = 0
    for i in char_map:
        if char_map[i] > largest_string_occurrence:
            largest_string = [i]
            largest_string_occurrence = char_map[i]
        if char_map[i] == largest_string_occurrence:
            largest_string.append(i)
    return ",".join(set(largest_string))


def find_max_char_2(string):
    char_map = {}
    for i in string:
        if i not in char_map:
            char_map[i] = 1
        else:
            char_map[i] += 1
    largest_string = []
    largest_string_occurrence = 0
    for i in char_map:
        if char_map[i] > largest_string_occurrence:
            largest_string = [i]
            largest_string_occurrence = char_map[i]
        if char_map[i] == largest_string_occurrence:
            largest_string.append(i)
    return ",".join(set(largest_string))


input_string = input()
print(find_max_char_1(input_string))
print(find_max_char_2(input_string))

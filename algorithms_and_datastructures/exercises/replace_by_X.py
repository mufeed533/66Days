"""
Given a string and a pattern, Replace all the continuous occurrence of pattern with a single X in the string. For a clear view see the example below.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is string str.
The second line of each test case contains a string s,which is a pattern.

Output:

Print the modified string str.

Constraints:

1 ≤ T ≤ 100
1 ≤ size of str,s ≤ 1000

Example:

Input
2
abababcdefababcdab
ab
geeksforgeeks
geeks

Output
XcdefXcdX
XforX
"""


def replace_by_x_1(string, pattern):  # straight forward solution
    pattern_len = len(pattern)
    i = 0
    output_string = " "
    while i <= len(string) - 1:
        if string[i: i + pattern_len] == pattern:
            if output_string[-1] != "X":
                output_string += "X"
            i = i + pattern_len
        else:
            output_string += string[i]
            i += 1
    return output_string.strip()


def replace_by_x_2(string, pattern):  # using python libraries/shortcut
    import re
    string = string.replace(pattern, "X")
    string = re.sub(r"X{2,}", "X", string)
    return string


t = int(input())  # test cases
while t != 0:
    raw_string = input()
    pattern = input()
    print(replace_by_x_2(raw_string, pattern))
    t -= 1

"""
Reverse an input string
"""

input_string = str(input())

output_string = ""
for i in range(len(input_string)-1, -1, -1):
    output_string += input_string[i]
print(output_string)

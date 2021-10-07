"""
Divide an array into an array of sub arrays with length n
ex:
array : [1,2,3,4,5]
chunk size : [2]
output : [[1,2], [3,4], [5]]
"""

input_array = list(map(int, input().split(" ")))
chunk_size = int(input())

output_list = []

for i in range(0, len(input_array), chunk_size):
    output_list.append(input_array[i:i + chunk_size])
print(output_list)

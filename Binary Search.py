with open('새파일.txt') as file:
    lines = []
    for line in file:
        lines.append(line.split())

sorted_array = []
given_array = []

for i in lines[2]:
    sorted_array.append(int(i))

for i in lines[3]:
    given_array.append(int(i))

def binary_search(sorted_array, given_array, i):
    start_index = 0
    end_index = len(sorted_array) - 1
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        index_value = sorted_array[mid_index]
        if index_value == given_array[i]:
            return mid_index + 1
        elif index_value < given_array[i]:
            start_index = mid_index + 1
        elif index_value > given_array[i]:
            end_index = mid_index - 1
    return -1

for i in range(len(given_array)):
    print(binary_search(sorted_array, given_array, i), end = ' ')

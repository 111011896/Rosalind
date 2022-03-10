with open('새파일.txt') as file:
    lines = []
    for line in file:
        lines.append(line.split())

arr = []

for i in lines[1]:
    arr.append(int(i))

print(arr)

pivot = arr[0]
lesser_arr, equal_arr, greater_arr = [], [], []

for i in arr:
    if i < pivot:
        lesser_arr.append(i)
    elif i > pivot:
        greater_arr.append(i)
    else:
        equal_arr.append(i)

total_arr = lesser_arr + equal_arr + greater_arr

for i in total_arr:
    print(i, end=' ')

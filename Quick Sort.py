with open('새파일.txt') as file:
    lines = []
    for line in file:
        lines.append(line.split())

arr = []

for i in lines[1]:
    arr.append(int(i))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for i in arr:
        if i < pivot:
            lesser_arr.append(i)
        elif i > pivot:
            greater_arr.append(i)
        else:
            equal_arr.append(i)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

for i in quick_sort(arr):
    print(i, end=' ')

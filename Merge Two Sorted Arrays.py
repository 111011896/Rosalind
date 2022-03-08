with open('새파일.txt') as file:
    lines = []
    for line in file:
        lines.append(line.split())

array = []

for i in range(len(lines)):
    if i % 2 != 0:
        for j in lines[i]:
            array.append(int(j))
    else:
        pass

for i in range(len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

for i in array:
    print(i, end=' ')

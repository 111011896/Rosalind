with open('새파일.txt') as file:
    lines = []
    for line in file:
        lines.append(line.split())

array = []

for i in lines[1]:
    array.append(int(i))

n = 0

for i in range(len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            n += 1
        else:
            break

print(n)

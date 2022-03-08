with open('새파일.txt') as file:
    lines = []
    for line in file:
        lines.append(line.split())

array = []
array_set = []

for i in lines:
    lst = []
    for j in range(len(i)):
        lst.append(int(i[j]))
    array.append(lst)
    array_set.append(list(set(lst)))

for i in range(len(array)):
    l = len(array[i])
    blink = []
    for k in range(len(array_set[i])):
        if array[i].count(array_set[i][k]) > (l/2):
            blink.append(array_set[i][k])
        elif array[i].count(array_set[i][k]) == (l/2):
            pass
        elif array[i].count(array_set[i][k]) < (l/2):
            blink.append(-1)
    if not blink:
        pass
    else:
        print(max(blink))

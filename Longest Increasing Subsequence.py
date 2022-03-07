with open('새파일.txt') as file:
    lines = []
    for line in file:
        lines.append(line.split())

lst = lines[1]
ori_sequence = []

for i in lst:
    ori_sequence.append(int(i))

final = []

for i in range(len(ori_sequence)):
    blinks = []
    first_sequence = ori_sequence[i:]
    for j in range(len(first_sequence)):
        blink = []
        blink.append(first_sequence[0])
        second_sequence = first_sequence[j:]
        for k in range(len(second_sequence)):
            if blink[-1] < second_sequence[k]:
                blink.append(second_sequence[k])
            else:
                pass
        blinks.append(blink)
    final.append(blinks)

lst = []

for i in range(len(final)):
    lst.append(max(final[i], key=len))

increasing = max(lst, key=len)

final = []

for i in range(len(ori_sequence)):
    blinks = []
    first_sequence = ori_sequence[i:]
    for j in range(len(first_sequence)):
        blink = []
        blink.append(first_sequence[0])
        second_sequence = first_sequence[j:]
        for k in range(len(second_sequence)):
            if blink[-1] > second_sequence[k]:
                blink.append(second_sequence[k])
            else:
                pass
        blinks.append(blink)
    final.append(blinks)

lst = []

for i in range(len(final)):
    lst.append(max(final[i], key=len))

decreasing = max(lst, key=len)

for i in increasing:
    print(i, end=' ')
print('')

for i in decreasing:
    print(i, end=' ')
print('')

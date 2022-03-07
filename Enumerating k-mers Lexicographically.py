with open('새파일.txt') as file:
    files = file.readlines()
    ATGC = files[0].split()
    count = int(files[1])

import itertools

nPr = list(itertools.product(ATGC, repeat = count))

list = []

for i in range(len(nPr)):
    blink = ''
    for k in range(count):
        blink += nPr[i][k]
    list.append(blink)

for i in sorted(list):
    print(i)

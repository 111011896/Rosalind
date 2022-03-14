with open('새파일.txt') as file:
    lines = []
    empty = ''
    for line in file:
        if line.startswith('>'):
            lines.append(empty)
            empty = ''
        else:
            empty += line.rstrip()
    lines.append(empty)

sequence = lines[1]

import itertools

k = 4
product = list(itertools.product('ACGT', repeat = k))

lst = []

for i in product:
    string = ''
    for j in i:
        string += j
    lst.append(string)

dic = {}

for i in lst:
    dic[i] = 0

for i in range(len(sequence)-k+1):
    if sequence[i:i+k] in lst:
        if not sequence[i:i+k] in dic:
            dic[sequence[i:i+k]] = 0
        else:
            dic[sequence[i:i+k]] += 1
    else:
        pass

for key, value in sorted(dic.items()):
    print(value, end=' ')

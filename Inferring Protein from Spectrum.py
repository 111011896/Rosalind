with open('새파일.txt') as file:
    lines1 = []
    for line in file:
        lines1.append(line.split())

with open('개새파일.txt') as file:
    lines2 = []
    for line in file:
        lines2.append(line.split())

dic = {}

for i in lines2:
    dic[i[0]] = round(float(i[1]), 2)

flt = []

for i in lines1:
    flt.append(float(i[0]))

gap = []

for i in range(len(flt)-1):
    gap.append(round(flt[i+1] - flt[i], 2))

str = ""

for i in range(len(gap)):
    for key, value in dic.items():
        if value == gap[i]:
            str += key
            break

print(str)

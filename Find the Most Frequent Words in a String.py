with open('새파일.txt') as file:
    lines = []
    for line in file:
        lines.append(line.rstrip())

text = lines[0]
k = int(lines[1])

dic = {}

for i in range(len(text)-k+1):
    if text[i:i+k] not in dic:
        dic[text[i:i+k]] = 0
    else:
        dic[text[i:i+k]] += 1

dic = dict(sorted(dic.items()))

for key, value in dic.items():
    if value == max(dic.values()):
        print(key, end=' ')

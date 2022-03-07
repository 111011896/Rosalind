with open("새파일.txt") as f:
    text = f.read()

import re
p = re.compile("Rosalind[_]\d{4}")
title = p.findall(text)

blink = []

for i in range(len(title)):
    text = text.replace(title[i], '/')

content = text.split("/")[1:]

for i in range(len(content)):
    content[i] = content[i].replace('\n', '')

blink = []

for i in range(len(content)):
  G = content[i].count("G")
  C = content[i].count("C")
  A = content[i].count("A")
  T = content[i].count("T")
    blink.append(round((G + C) / (A + T + G + C) * 100, 6))

dic = {}

for i in range(len(title)):
    dic[title[i]] = blink[i]

for i in range(len(title)):
    if dic[title[i]] == max(list(dic.values())):
        print(str(title[i]) + '\n' + "%0.6f" % dic[title[i]])

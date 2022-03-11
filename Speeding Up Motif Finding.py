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

pattern = lines[1]
lps = {}

def computeLPS(pat, lps):
    leng = 0
    lps[0] = 0
    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1

computeLPS(pattern, lps)
values = list(lps.values())

for i in values:
    print(i, end=' ')

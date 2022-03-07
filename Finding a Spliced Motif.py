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

lines = lines[1:]

original_string = lines[0]
subsequence = lines[1]

n = 0
blink = []

for i in range(len(subsequence)):
    if i == 0:
        original_string = original_string[::]
        n = original_string.find(subsequence[i])
        blink.append(n)
    else:
        original_string = original_string[n+1:]
        n = original_string.find(subsequence[i])
        blink.append(n+1)

n = 0

for i in blink:
    n += i
    print(n+1, end=' ')

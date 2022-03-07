with open("새파일.txt") as f:
    text = f.read()

text = text.replace('\n', ' ')
text = text.replace(' ', '')
text = text.split(">")
text = text[1:]

blink = []

for i in range(len(text)):
    blink.append(text[i][13:])

list = []

for k in range(len(blink[0])):
    sub = []
    A = 0
    C = 0
    G = 0
    T = 0
    for i in range(len(blink)):
        if blink[i][k] == "A":
            A += 1
        elif blink[i][k] == "C":
            C += 1
        elif blink[i][k] == "G":
            G += 1
        elif blink[i][k] == "T":
            T += 1
    sub.append(A)
    sub.append(C)
    sub.append(G)
    sub.append(T)
    list.append(sub)

final = ''

for i in range(len(list)):
    if list[i].index(max(list[i])) == 0:
        final += "A"
    if list[i].index(max(list[i])) == 1:
        final += "C"
    if list[i].index(max(list[i])) == 2:
        final += "G"
    if list[i].index(max(list[i])) == 3:
        final += "T"

print(final)

for k in range(len(list[0])):
    new_blink = ''
    for i in range(len(list)):
        new_blink += str(list[i][k]) + ' '
        if i != len(list) - 1:
            pass
        elif k == 0:
            print('A:', new_blink)
        elif k == 1:
            print('C:', new_blink)
        elif k == 2:
            print('G:', new_blink)
        elif k == 3:
            print('T:', new_blink)

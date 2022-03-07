with open('새파일.txt') as file:
    blink = []
    empty = ''
    for line in file:
        if line.startswith('>'):
            blink.append(empty)
            empty = ''
        else:
            empty += line.rstrip()
    blink.append(empty)

string1 = blink[1]
string2 = blink[2]

transitions = 0
transversions = 0
normal = 0

for i in range(len(string1)):
    if string1[i] == string2[i]:
        normal += 1
    elif string1[i] == "A" and string2[i] == "G":
        transitions += 1
    elif string1[i] == "G" and string2[i] == "A":
        transitions += 1
    elif string1[i] == "C" and string2[i] == "T":
        transitions += 1
    elif string1[i] == "T" and string2[i] == "C":
        transitions += 1
    else:
        transversions += 1

print(round(transitions / transversions, 11))

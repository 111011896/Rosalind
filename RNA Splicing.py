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

blink = blink[1:]
exon = blink[0]

for i in range(1, len(blink)):
    exon = exon.replace(blink[i], '')

exon = exon.replace("T", "U")

with open("개새파일.txt") as f:
    text = f.read()

text = text.replace('\n', '      ')
text = text.replace('      ', ' ')
text = text.split(' ')

dic = {}

for i in range(len(text)-1):
    if i % 2 == 0:
        dic[text[i]] = text[i+1]

protein = ''

for i in range(1, len(exon)+1):
    if i % 3 != 0:
        protein += exon[i-1]
    else:
        protein += (exon[i-1] + " ")

new_text = protein.split(" ")[0:-1]

protein = ''

for i in range(len(new_text)):
    if dic[new_text[i]] == "Stop":
        break
    protein += dic[new_text[i]]

print(protein)

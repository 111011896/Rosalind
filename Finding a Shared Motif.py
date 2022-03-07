with open("새파일.txt") as f:
    text = f.read()

text = text.replace('\n', ' ')
text = text.replace(' ', '')
text = text.split(">")
text = text[1:]

blink = []
for i in range(len(text)):
    blink.append(text[i][13:])

def all_find(i):
    lst = list()
    for k in range(len(blink[i])+1):
        for j in range(len(blink[i])+1):
            lst.append(blink[i][k:j])
    return set(lst)

subset = list()

for i in range(len(blink)-1):
    if i == 0:
        subset.append(all_find(i) & all_find(i+1))
    elif i != 0:
        subset.append(all_find(i+1) & subset[i-1])

subset = list(subset[-1])
lenth = []

for i in range(len(subset)):
    lenth.append(len(subset[i]))

for i in range(len(subset)):
    if len(subset[i]) == max(lenth):
        print(subset[i])

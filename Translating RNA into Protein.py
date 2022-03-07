with open("새파일.txt") as f:
    text = f.read()

text = text.replace('\n', '      ')
text = text.replace('      ', ' ')
text = text.split(' ')

dic = {}

for i in range(len(text)-1):
    if i % 2 == 0:
        dic[text[i]] = text[i+1]

with open("개새파일.txt") as f:
    new_text = f.read()

blink = ''

for i in range(1, len(new_text)+1):
    if i % 3 != 0:
        blink += new_text[i-1]
    else:
        blink += (new_text[i-1] + " ")

new_text = blink.split(" ")[0:-1]

blink = ''

for i in range(len(new_text)):
    if dic[new_text[i]] == "Stop":
        break
    blink += dic[new_text[i]]

print(blink)

text = ''

with open("새파일.txt") as file:
    lines = file.readlines()
    for line in lines[1:]:
        text += line.rstrip()

reverse = ""
for i in range(len(text)):
    if text[i] == "A":
        reverse += "T"
    elif text[i] == "C":
        reverse += "G"
    elif text[i] == "T":
        reverse += "A"
    elif text[i] == "G":
        reverse += "C"

reverse = reverse[::-1]
print(len(text))

for i in range(len(text)):
    for j in range(len(text)):
        if i == 0:
            if text[0:j] == reverse[-j:]:
                if j >= 4 and j <= 12 and i+j <= len(text):
                    print(i+1, j)
        if text[i:i+j] == reverse[-i-j:-i]:
            if j >= 4 and j <= 12 and i+j <= len(text):
                print(i+1, j)

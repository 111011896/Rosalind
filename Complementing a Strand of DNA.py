with open("새파일.txt") as f:
    text = f.read()

blink = ""

for i in range(len(text)):
    if text[i] == "A":
        blink += "T"
    elif text[i] == "C":
        blink += "G"
    elif text[i] == "T":
        blink += "A"
    elif text[i] == "G":
        blink += "C"

print(blink[::-1])

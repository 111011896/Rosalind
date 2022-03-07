f = open("새파일.txt")

lines = f.readlines()
line1 = lines[0].rstrip('\n')
line2 = lines[1].rstrip('\n')

num = 0

for i in range(len(line1)):
    if line1[i] != line2[i]:
        num += 1

print(num)

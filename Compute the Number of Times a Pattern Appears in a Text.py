with open('새파일.txt') as file:
    lines = []
    for line in file:
        lines.append(line.rstrip())

text = lines[0]
pattern = lines[1]

def PatternCount(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

print(PatternCount(text,pattern))

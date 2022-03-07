with open('새파일.txt') as file:
    alpha = []
    digit = []
    for line in file:
        split = line.split("   ")
        alpha.append(split[0])
        digit.append(float(split[1]))

dataset = "SKADYEK"
total_mass = 0

for i in range(len(dataset)):
    for j in range(len(alpha)):
        if dataset[i] == alpha[j]:
            total_mass += digit[j]

print(round(total_mass, 3))

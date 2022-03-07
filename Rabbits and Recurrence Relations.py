n = 28
k = 2
kid = [1]
adult = [0]

for i in range(n):
    adult.append(adult[i] + kid[i])
    kid.append(k * adult[i])

print(adult[n-1] + kid[n-1])

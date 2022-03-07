n = 95
m = 19
kid = [1]
adult = [0]

for i in range(n):
    if i < m-1:
        adult.append(adult[i] + kid[i])
        kid.append(adult[i])
    elif i >= m-1:
        adult.append(adult[i] + kid[i] - kid[i+1-m])
        kid.append(adult[i])

print(adult[n-1] + kid[n-1])

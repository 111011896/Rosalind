import itertools

array = []
n = 7

for i in range(n):
    array.append(i+1)

permutation = itertools.permutations(array, len(array))
permutation = list(permutation)

print(len(permutation))

for i in list(permutation):
    for k in range(len(i)):
        print(list(i)[k], end = ' ')
    print('')

import itertools

n = 5
lst = []

for i in range(1, n+1):
    lst.append(i)
    lst.append(-i)

lst = sorted(lst)

nPr = itertools.permutations(lst, n)
collect = []

for i in nPr:
    collect.append(list(i))

blinks = []

for i in collect:
    blink = []
    for k in range(len(i)):
        blink.append(abs(i[k]))
    if len(set(blink)) == n:
        blinks.append(i)
    else:
        pass

print(len(blinks))

for i in blinks:
    a, b, c, d, e = i
    print(a, b, c, d, e)
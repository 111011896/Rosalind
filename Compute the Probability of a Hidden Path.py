sequence = "BAAAAABBBABBBAAABABABBAAABABBBBBAAABBBAAABBBABAAAA"

A_A = 0.089
A_B = 0.911
B_A = 0.339
B_B = 0.661

initial = 0.5

for i in range(len(sequence)-1):
    if sequence[i] == "A" and sequence[i+1] == "A":
        initial *= A_A
    elif sequence[i] == "A" and sequence[i+1] == "B":
        initial *= A_B
    elif sequence[i] == "B" and sequence[i+1] == "A":
        initial *= B_A
    elif sequence[i] == "B" and sequence[i+1] == "B":
        initial *= B_B

print(round(initial, 35))

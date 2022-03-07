sequence1 = "BAABABBABBAABAAAAAABBABABBABBBBBBBABABBBAAABBBABAA"
sequence2 = "yzyzxxzyyxxzyxzzxyyxzyxzxxxxxxyyyzyxyzyxxxxyzyyxxy"

A_x = 0.56
A_y = 0.04
A_z = 0.399
B_x = 0.169
B_y = 0.578
B_z = 0.253

def select(sequence1, sequence2):
    if sequence1[0] == "A" and sequence2[0] == "x":
        initial = A_x
        return initial
    elif sequence1[0] == "A" and sequence2[0] == "y":
        initial = A_y
        return initial
    elif sequence1[0] == "A" and sequence2[0] == "z":
        initial = A_z
        return initial
    elif sequence1[0] == "B" and sequence2[0] == "x":
        initial = B_x
        return initial
    elif sequence1[0] == "B" and sequence2[0] == "y":
        initial = B_y
        return initial
    elif sequence1[0] == "B" and sequence2[0] == "z":
        initial = B_z
        return initial

initial = select(sequence1, sequence2)

for i in range(len(sequence1)-1):
    if sequence1[i+1] == "A" and sequence2[i+1] == "x":
        initial *= A_x
    elif sequence1[i+1] == "A" and sequence2[i+1] == "y":
        initial *= A_y
    elif sequence1[i+1] == "A" and sequence2[i+1] == "z":
        initial *= A_z
    elif sequence1[i+1] == "B" and sequence2[i+1] == "x":
        initial *= B_x
    elif sequence1[i+1] == "B" and sequence2[i+1] == "y":
        initial *= B_y
    elif sequence1[i+1] == "B" and sequence2[i+1] == "z":
        initial *= B_z

print(round(initial, 43))

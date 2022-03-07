with open("새파일.txt") as f:
    text = f.read()

text = text.split(' ')

rand_var = [0, 1, 2]
total = 0

P_dom_AA_AA = 1
P_dom_AA_Aa = 1
P_dom_AA_aa = 1
P_dom_Aa_Aa = 0.75
P_dom_Aa_aa = 0.5
P_dom_aa_aa = 0

for i in range(len(text)):
    if i == 0:
        total += (rand_var[0] * (1 - P_dom_AA_AA) ** 2 + rand_var[1] * 2 * P_dom_AA_AA * (1 - P_dom_AA_AA) + rand_var[2] * (P_dom_AA_AA) ** 2) * int(text[i])
    elif i == 1:
        total += (rand_var[0] * (1 - P_dom_AA_Aa) ** 2 + rand_var[1] * 2 * P_dom_AA_Aa * (1 - P_dom_AA_Aa) + rand_var[2] * (P_dom_AA_Aa) ** 2) * int(text[i])
    elif i == 2:
        total += (rand_var[0] * (1 - P_dom_AA_aa) ** 2 + rand_var[1] * 2 * P_dom_AA_aa * (1 - P_dom_AA_aa) + rand_var[2] * (P_dom_AA_aa) ** 2) * int(text[i])
    elif i == 3:
        total += (rand_var[0] * (1 - P_dom_Aa_Aa) ** 2 + rand_var[1] * 2 * P_dom_Aa_Aa * (1 - P_dom_Aa_Aa) + rand_var[2] * (P_dom_Aa_Aa) ** 2) * int(text[i])
    elif i == 4:
        total += (rand_var[0] * (1 - P_dom_Aa_aa) ** 2 + rand_var[1] * 2 * P_dom_Aa_aa * (1 - P_dom_Aa_aa) + rand_var[2] * (P_dom_Aa_aa) ** 2) * int(text[i])
    elif i == 5:
        total += (rand_var[0] * (1 - P_dom_aa_aa) ** 2 + rand_var[1] * 2 * P_dom_aa_aa * (1 - P_dom_aa_aa) + rand_var[2] * (P_dom_aa_aa) ** 2) * int(text[i])

print(total)

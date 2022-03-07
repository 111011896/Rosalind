def factorial(n):
    f = 1
    for num in range(n, 0, -1):
        f *= num
    return f

def combination(n, r):
    return int(factorial(n) / factorial(r) / factorial(n-r))

def permutation(n, r):
    return int(factorial(n) / factorial(n-r))

k = 26
m = 23
n = 20

P_AA_AA = combination(k, 2) * 1
P_AA_Aa = k * m * 1
P_AA_aa = k * n * 1
P_Aa_Aa = combination(m, 2) * 0.75
P_Aa_aa = m * n * 0.5
P_aa_aa = combination(n, 2) * 0

total = combination(k+m+n, 2)

P_total = (P_AA_AA + P_AA_Aa + P_AA_aa + P_Aa_Aa + P_Aa_aa + P_aa_aa) / total

print("%0.5f" % P_total)

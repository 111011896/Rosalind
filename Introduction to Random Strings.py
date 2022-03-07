with open('새파일.txt') as file:
    lines = []
    for line in file:
        lines.append(line.split())

ATGC_string = lines[0][0]
CG_rate_array = []

for i in lines[1]:
    CG_rate_array.append(float(i))

import math

def random_string(ATGC_string, CG_rate_array, i):
    CG_count = ATGC_string.count("C") + ATGC_string.count("G")
    AT_count = ATGC_string.count("A") + ATGC_string.count("T")
    common_logarithm = math.log10(((CG_rate_array[i] / 2) ** CG_count) * (((1 - CG_rate_array[i]) / 2) ** AT_count))
    return round(common_logarithm, 3)

for i in range(len(CG_rate_array)):
    print(random_string(ATGC_string, CG_rate_array, i), end = ' ')

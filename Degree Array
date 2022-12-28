with open('test.txt') as file:
    lines = []
    for line in file:
        lines.append(line.split())

vertices_dic = {}

for sets in lines[1:]:
    node1 = int(sets[0])
    node2 = int(sets[1])
    if node1 not in vertices_dic.keys():
        vertices_dic[node1] = 1
    else:
        vertices_dic[node1] += 1
    if node2 not in vertices_dic.keys():
        vertices_dic[node2] = 1
    else:
        vertices_dic[node2] += 1

vertices_dic = sorted(vertices_dic.items())
answer = ""

for sets in vertices_dic:
    if sets[1] > 1:
        answer += str(sets[1]) + " "

print(answer.rstrip())

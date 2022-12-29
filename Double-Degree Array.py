with open('test.txt') as file:
    lines = []
    for line in file:
        lines.append(line.split())

node_count = int(lines[0][0])
vertices_dic = {}

for i in range(1, node_count+1):
    for sets in lines[1:]:
        node1 = int(sets[0])
        node2 = int(sets[1])
        if i == node1:
            if node1 not in vertices_dic.keys():
                vertices_dic[node1] = 1
            else:
                vertices_dic[node1] += 1
        if i == node2:
            if node2 not in vertices_dic.keys():
                vertices_dic[node2] = 1
            else:
                vertices_dic[node2] += 1

for i in range(1, node_count+1):
    if i not in vertices_dic.keys():
        vertices_dic[i] = 0

answer = ""

for i in range(1, node_count+1):
    adjacency_dic = {}
    sum = 0
    for sets in lines[1:]:
        node1 = int(sets[0])
        node2 = int(sets[1])
        if node1 == i:
            adjacency_dic[node2] = 1
        else:
            pass
        if node2 == i:
            adjacency_dic[node1] = 1
        else:
            pass
    for j in range(1, node_count+1):
        if j not in adjacency_dic.keys():
            adjacency_dic[j] = 0
    for k in range(1, node_count+1):
        if adjacency_dic[k] == 1:
            sum += vertices_dic[k]
        else:
            sum += 0
    answer += str(sum) + " "

print(answer.rstrip())

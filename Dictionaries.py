with open("새파일.txt") as f:
    text = f.read()

text = text.split(' ')
dic = {}

for i in range(len(text)):
    dic[text[i]] = text.count(text[i])

dic_keys = list(dic.keys())
dic_values = list(dic.values())

for i in range(len(dic_keys)):
    print(str(dic_keys[i]) + ' ' + str(dic_values[i]))

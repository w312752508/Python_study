import json
dic = {}
with open('haproxy') as f:
    for i in f:
        if i[0] not in [' ', '\t']:
            dic[i] = []
            lst = dic[i]
        else:
             lst.append(i)
print("dic>>",type(dic))
for k in dic :
    print("k>>",type(k))
    k_str = json.dumps(k)
    print("k_str>>",type(k_str))
# inp = input('请输入内容：')
# for i in dic:
#     if i.startswith('backend'):
#         if i.find(inp) != -1:
#             for j in dic[i]:
#                 print(j, end='')


#!/sur/bin/evn python
# -*- coding:utf-8 -*-
import json
dit_f = {}
r = json.load(open('dep_subnet', 'r', encoding='utf-8'))
with open('source_ip','r') as f1:
    for i in f1:
        i = i.strip()
        if i in r.keys():
            k = r[i]
            if k in dit_f.keys():
                dit_f[k] = dit_f[k] + 1
            else:
                dit_f[k] = 1
    f1.close()
with open('ip_online', 'w',encoding='utf-8') as f2:
    for k,v in dit_f.items():
        online_num = "%s的在线数是%s\n" %(k,v)
        f2.write(online_num)
    # f2.close()

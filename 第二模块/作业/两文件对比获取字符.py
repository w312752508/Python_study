#!/usr/bin/env python
# coding:utf8


file1 = 'file01'
file2 = 'file02'
file3 = 'file03'

flag = {}
obj3 = open(file3, 'w')

with open(file1, 'rU') as obj1, open(file2, 'rU') as obj2:
    for i in obj1:
        if i == '\n':
            continue
        for j in obj2:
            if j.find(i.strip()) != -1:
                if not flag.get(j, 0):
                    obj3.write(j)
                flag[j] = 1
        obj2.seek(0)



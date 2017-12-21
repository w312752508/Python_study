with open("test_file", "r", encoding="utf-8") as f, \
        open("test_file_bak", "w", encoding="utf-8") as f_new:
    for line in f:
        f_new.write(line)
f = open("test_file","w",encoding="utf-8")
f_new = open("test_file_bak","r",encoding="utf-8")
f.seek(0)
for line in f_new:
    if "负载均衡" in line :
        line = line.replace("负载均衡","SLB")
    f.write(line)
    f.flush()
import re
# a = re.search('(.{6})(\d{8})(\d{4})',"&!sd261198512104489")
# print(a.group())
# print(a.groups())
# print(a.groupsdic())

# print(re.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group())
# print(re.search("\s+","ab\tc1\n3").group())
# print("dd")

# a = re.search('addr:([\d.]*)',"inet addr:10.230.38.114  网关:10.230.38.255").groups()
# a = re.search('关+',"inet addr:10.230.38.114  网关:10.230.38.255").group()
# print(a)
# # print(a.group())

# print(re.search('\d','ab3cd 45 fea33s d63').groupoup())
print(re.search('\d+','ab3456cd 45 fea33s d63').group())
# print(re.findall('\d+','ab3cd45fe3as33d6'))
# print(re.findall('\d','ab3cd45fe3as33d6'))
# print(re.findall("ab*","cabb3abcbbac"))
# print(re.findall('\d','ab3c\nd45\nfeasd6',flags=re.MULTILINE))
# print(re.findall('\d+','ab3c\nd45\nfeasd6',flags=re.MULTILINE))
# print(re.split('\\\\',r'd:\asf\abc\test.text'))

# print(re.findall("ab","ab+cd+abb+bba"))
# print(re.findall("ab+","ab+cd+abb+bba"))
# print(re.findall("\s+","ab\tc\t1\n3"),"##")
# print(re.search("\s","ab\tc\t1\n3").group(),"##")

# print(re.search("(abc){2}a(123|456)c", "abcabca456c").group())
# print(re.search("(abc){2}a(123|456)c", "abcabca456c").groups())